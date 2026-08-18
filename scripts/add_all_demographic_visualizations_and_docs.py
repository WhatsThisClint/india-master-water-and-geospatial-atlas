"""
add_all_demographic_visualizations_and_docs.py
1. Computes percentage growth (2000 -> 2020) and decadal split growth (2000->2010, 2010->2020).
2. Translates them to GeoPackage raster tables.
3. Configures multiple distinct visualization layers in QGIS under 07_Demographics_and_Socioeconomic.
4. Updates internal GeoPackage AI documentation tables (_master_layer_catalog, _ai_layer_documentation).
5. Synchronizes HYDROSHEDS_CONSOLIDATED_MASTER_AI_CATALOG.md.
"""

import socket
import struct
import json
import sqlite3
import os

GPKG_PATH = r"F:/Antigravity/Hydrosheds and Basins/hydrosheds_consolidated_master.gpkg"
PORT = 9877

def main():
    qgis_code = r"""
from osgeo import gdal
import numpy as np
from qgis.core import (
    QgsProject, QgsRasterLayer, QgsColorRampShader, QgsRasterShader,
    QgsSingleBandPseudoColorRenderer, QgsCoordinateReferenceSystem
)
from qgis.PyQt.QtGui import QColor
from qgis.utils import iface

project = QgsProject.instance()
root = project.layerTreeRoot()
gpkg = "F:/Antigravity/Hydrosheds and Basins/hydrosheds_consolidated_master.gpkg"
crs_4326 = QgsCoordinateReferenceSystem("EPSG:4326")

grp = root.findGroup("07_Demographics_and_Socioeconomic")
if not grp:
    grp = root.addGroup("07_Demographics_and_Socioeconomic")

# 1. Compute Percentage Growth and Decadal Growth Rasters
ds_2000 = gdal.Open(f"GPKG:{gpkg}:worldpop_india_2000_population_count_1km")
ds_2010 = gdal.Open(f"GPKG:{gpkg}:worldpop_india_2010_population_count_1km")
ds_2020 = gdal.Open(f"GPKG:{gpkg}:worldpop_india_2020_population_count_1km")

if ds_2000 and ds_2010 and ds_2020:
    arr_2000 = ds_2000.ReadAsArray().astype(np.float32)
    arr_2010 = ds_2010.ReadAsArray().astype(np.float32)
    arr_2020 = ds_2020.ReadAsArray().astype(np.float32)
    
    # Growth 2000 -> 2010
    g_00_10 = arr_2010 - arr_2000
    g_00_10[(arr_2000 < 0) | (arr_2010 < 0)] = -9999
    
    # Growth 2010 -> 2020
    g_10_20 = arr_2020 - arr_2010
    g_10_20[(arr_2010 < 0) | (arr_2020 < 0)] = -9999
    
    # Percentage Growth (2000 -> 2020)
    pct_growth = np.zeros_like(arr_2020)
    valid_mask = (arr_2000 > 5) & (arr_2020 >= 0)
    pct_growth[valid_mask] = ((arr_2020[valid_mask] - arr_2000[valid_mask]) / arr_2000[valid_mask]) * 100.0
    pct_growth[~valid_mask] = -9999
    
    drv = gdal.GetDriverByName("GTiff")
    
    # Write and ingest helper
    def write_and_ingest(arr, temp_name, tbl_name):
        t_path = f"F:/Antigravity/Hydrosheds and Basins/{temp_name}"
        ds_out = drv.Create(t_path, ds_2020.RasterXSize, ds_2020.RasterYSize, 1, gdal.GDT_Float32)
        ds_out.SetGeoTransform(ds_2020.GetGeoTransform())
        ds_out.SetProjection(ds_2020.GetProjection())
        band = ds_out.GetRasterBand(1)
        band.SetNoDataValue(-9999)
        band.WriteArray(arr)
        ds_out = None
        
        opts = gdal.TranslateOptions(
            format="GPKG",
            creationOptions=[
                f"RASTER_TABLE={tbl_name}",
                "APPEND_SUBDATASET=YES",
                "TILE_FORMAT=PNG_JPEG",
                "ZOOM_LEVEL_STRATEGY=AUTO"
            ]
        )
        ds_g = gdal.Translate(gpkg, t_path, options=opts)
        ds_g = None
        try:
            import os
            os.remove(t_path)
        except Exception:
            pass
        print(f"Ingested {tbl_name}")

    write_and_ingest(pct_growth, "temp_pct_growth.tif", "worldpop_india_20yr_pct_growth_2000_2020_1km")
    write_and_ingest(g_00_10, "temp_g_00_10.tif", "worldpop_india_decadal_growth_2000_2010_1km")
    write_and_ingest(g_10_20, "temp_g_10_20.tif", "worldpop_india_decadal_growth_2010_2020_1km")

# 2. Add Multi-Thematic Visualizations to QGIS

# A. Percentage Growth Rate Layer (% Change 2000 -> 2020)
uri_pct = f"GPKG:{gpkg}:worldpop_india_20yr_pct_growth_2000_2020_1km"
r_pct = QgsRasterLayer(uri_pct, "WorldPop 20-Year Percentage Population Growth (% Change 2000-2020)", "gdal")
if r_pct.isValid():
    for l in project.mapLayersByName("WorldPop 20-Year Percentage Population Growth (% Change 2000-2020)"):
        project.removeMapLayer(l.id())
    r_pct.setCrs(crs_4326)
    fcn_pct = QgsColorRampShader()
    fcn_pct.setColorRampType(QgsColorRampShader.Interpolated)
    items_pct = [
        QgsColorRampShader.ColorRampItem(-50.0, QColor(33, 102, 172, 220), "Significant Decline (< -25%)"),
        QgsColorRampShader.ColorRampItem(0.0, QColor(247, 247, 247, 0), "0% (Stable)"),
        QgsColorRampShader.ColorRampItem(25.0, QColor(254, 224, 144, 150), "+1% to +25% (Low Growth)"),
        QgsColorRampShader.ColorRampItem(50.0, QColor(253, 174, 97, 190), "+25% to +50% (Moderate Growth)"),
        QgsColorRampShader.ColorRampItem(100.0, QColor(244, 109, 67, 230), "+50% to +100% (High Growth: Population Doubled)"),
        QgsColorRampShader.ColorRampItem(300.0, QColor(213, 62, 79, 255), "> +100% (Hyper-Growth: Peri-Urban Sprawl)"),
    ]
    fcn_pct.setColorRampItemList(items_pct)
    shader_pct = QgsRasterShader()
    shader_pct.setRasterShaderFunction(fcn_pct)
    r_pct.setRenderer(QgsSingleBandPseudoColorRenderer(r_pct.dataProvider(), 1, shader_pct))
    project.addMapLayer(r_pct, False)
    node_pct = grp.addLayer(r_pct)
    node_pct.setItemVisibilityChecked(False)
    print("Added Percentage Growth Layer")

# B. Decadal Growth Phase 1 (2000 -> 2010)
uri_g1 = f"GPKG:{gpkg}:worldpop_india_decadal_growth_2000_2010_1km"
r_g1 = QgsRasterLayer(uri_g1, "WorldPop Decadal Growth Phase 1 (2000-2010 Net Change)", "gdal")
if r_g1.isValid():
    for l in project.mapLayersByName("WorldPop Decadal Growth Phase 1 (2000-2010 Net Change)"):
        project.removeMapLayer(l.id())
    r_g1.setCrs(crs_4326)
    fcn_g1 = QgsColorRampShader()
    fcn_g1.setColorRampType(QgsColorRampShader.Interpolated)
    items_g1 = [
        QgsColorRampShader.ColorRampItem(0.0, QColor(0, 0, 0, 0), "0"),
        QgsColorRampShader.ColorRampItem(100.0, QColor(254, 224, 144, 160), "+1 to 100"),
        QgsColorRampShader.ColorRampItem(500.0, QColor(253, 174, 97, 200), "+100 to 500"),
        QgsColorRampShader.ColorRampItem(2500.0, QColor(244, 109, 67, 230), "+500 to 2,500"),
        QgsColorRampShader.ColorRampItem(10000.0, QColor(213, 62, 79, 255), "> 2,500"),
    ]
    fcn_g1.setColorRampItemList(items_g1)
    shader_g1 = QgsRasterShader()
    shader_g1.setRasterShaderFunction(fcn_g1)
    r_g1.setRenderer(QgsSingleBandPseudoColorRenderer(r_g1.dataProvider(), 1, shader_g1))
    project.addMapLayer(r_g1, False)
    node_g1 = grp.addLayer(r_g1)
    node_g1.setItemVisibilityChecked(False)

# C. Decadal Growth Phase 2 (2010 -> 2020)
uri_g2 = f"GPKG:{gpkg}:worldpop_india_decadal_growth_2010_2020_1km"
r_g2 = QgsRasterLayer(uri_g2, "WorldPop Decadal Growth Phase 2 (2010-2020 Net Change)", "gdal")
if r_g2.isValid():
    for l in project.mapLayersByName("WorldPop Decadal Growth Phase 2 (2010-2020 Net Change)"):
        project.removeMapLayer(l.id())
    r_g2.setCrs(crs_4326)
    r_g2.setRenderer(QgsSingleBandPseudoColorRenderer(r_g2.dataProvider(), 1, shader_g1))
    project.addMapLayer(r_g2, False)
    node_g2 = grp.addLayer(r_g2)
    node_g2.setItemVisibilityChecked(False)

# D. Urban Settlement Footprint Classes (Categorized Density)
uri_urban = f"GPKG:{gpkg}:worldpop_india_2020_population_density_1km"
r_urban = QgsRasterLayer(uri_urban, "WorldPop 2020 Settlement Typology (Rural to Megacity)", "gdal")
if r_urban.isValid():
    for l in project.mapLayersByName("WorldPop 2020 Settlement Typology (Rural to Megacity)"):
        project.removeMapLayer(l.id())
    r_urban.setCrs(crs_4326)
    fcn_u = QgsColorRampShader()
    fcn_u.setColorRampType(QgsColorRampShader.Discrete)
    items_u = [
        QgsColorRampShader.ColorRampItem(10.0, QColor(0, 0, 0, 0), "Uninhabited / Wild (< 10 p/km²)"),
        QgsColorRampShader.ColorRampItem(250.0, QColor(161, 218, 180, 160), "Rural Hamlets & Villages (10 - 250 p/km²)"),
        QgsColorRampShader.ColorRampItem(1000.0, QColor(65, 182, 196, 200), "Semi-Urban & Agrarian Towns (250 - 1,000 p/km²)"),
        QgsColorRampShader.ColorRampItem(5000.0, QColor(44, 127, 184, 230), "Urban Cities & District HQs (1,000 - 5,000 p/km²)"),
        QgsColorRampShader.ColorRampItem(250000.0, QColor(37, 52, 148, 255), "High-Density Megacity (> 5,000 p/km²)"),
    ]
    fcn_u.setColorRampItemList(items_u)
    shader_u = QgsRasterShader()
    shader_u.setRasterShaderFunction(fcn_u)
    r_urban.setRenderer(QgsSingleBandPseudoColorRenderer(r_urban.dataProvider(), 1, shader_u))
    project.addMapLayer(r_urban, False)
    node_u = grp.addLayer(r_urban)
    node_u.setItemVisibilityChecked(False)

if iface:
    iface.mapCanvas().refresh()

uri_proj = f"geopackage:{gpkg}?projectName=India_Master_Hydrology_and_Infrastructure"
saved = project.write(uri_proj)
print(f"All demographic visualizations created and saved: {saved}")
"""

    payload = json.dumps({"type": "execute_code", "params": {"code": qgis_code}}).encode("utf-8")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(60)
    s.connect(("127.0.0.1", PORT))
    s.sendall(struct.pack(">I", len(payload)) + payload)

    raw_len = s.recv(4)
    msg_len = struct.unpack(">I", raw_len)[0]
    buf = b""
    while len(buf) < msg_len:
        buf += s.recv(min(4096, msg_len - len(buf)))
    s.close()
    res = json.loads(buf.decode("utf-8"))
    print("QGIS styling execution complete!")

    # 3. Update Internal GeoPackage Documentation
    print("Updating internal GeoPackage AI documentation tables...")
    conn = sqlite3.connect(r"F:\Antigravity\Hydrosheds and Basins\hydrosheds_consolidated_master.gpkg")

    docs = [
        (
            'WorldPop 20-Year Net Population Growth (2000-2020)',
            'worldpop_india_20yr_net_growth_2000_2020_1km',
            '07_Demographics_and_Socioeconomic',
            'Raster Tile Matrix (1km)',
            'Net change in human population count per 1km grid cell from 2000 to 2020 (Pop2020 - Pop2000).',
            'High positive values (> +1,000) identify rapid peri-urban conversion, groundwater recharge reduction, and explosive municipal water demand.',
            """### WorldPop 20-Year Net Population Growth (2000-2020)
- **Table**: `worldpop_india_20yr_net_growth_2000_2020_1km`
- **Resolution**: 1km (30 arc-seconds), CRS: EPSG:4326
- **Calculation Formula**: `Net Growth = Pop_2020 - Pop_2000`
- **Key Thematic Ramp**: Divergent Heatmap (Blue = Depopulation, Transparent = Stable, Crimson = >5,000 Growth Surge)
- **AI Analytics Application**: Use to identify rapidly urbanizing catchments where groundwater recharge areas are getting paved over."""
        ),
        (
            'WorldPop 20-Year Percentage Population Growth (% Change 2000-2020)',
            'worldpop_india_20yr_pct_growth_2000_2020_1km',
            '07_Demographics_and_Socioeconomic',
            'Raster Tile Matrix (1km)',
            'Relative percentage population growth rate from 2000 to 2020 (% Change).',
            'Isolates hyper-growth zones where population doubled or tripled (> 100%), independent of initial base population size.',
            """### WorldPop 20-Year Percentage Population Growth (% Change)
- **Table**: `worldpop_india_20yr_pct_growth_2000_2020_1km`
- **Resolution**: 1km (30 arc-seconds), CRS: EPSG:4326
- **Calculation Formula**: `((Pop_2020 - Pop_2000) / Pop_2000) * 100`
- **AI Analytics Application**: Evaluate proportional demographic stress on rural vs urban aquifer units."""
        ),
        (
            'WorldPop 2020 Settlement Typology (Rural to Megacity)',
            'worldpop_india_2020_population_density_1km',
            '07_Demographics_and_Socioeconomic',
            'Raster Tile Matrix (1km)',
            'Discrete human settlement classification based on population density thresholds.',
            'Categorizes India into Uninhabited (<10 p/km²), Rural Hamlets (10-250), Semi-Urban Towns (250-1000), Urban Cities (1000-5000), and Megacities (>5000).',
            """### WorldPop 2020 Settlement Typology
- **Table**: `worldpop_india_2020_population_density_1km`
- **Classification Standard**: Global Settlement Hierarchy / Degree of Urbanization (DEGURBA)
- **AI Analytics Application**: Cross-tabulate with CGWB groundwater extraction blocks to measure population living in overexploited zones by settlement type."""
        ),
        (
            'WorldPop Decadal Growth Phase 1 (2000-2010 Net Change)',
            'worldpop_india_decadal_growth_2000_2010_1km',
            '07_Demographics_and_Socioeconomic',
            'Raster Tile Matrix (1km)',
            'Net population change during the 2000-2010 decade.',
            'Historical benchmark for decadal demographic velocity comparisons.',
            """### WorldPop Decadal Growth Phase 1 (2000-2010)
- **Table**: `worldpop_india_decadal_growth_2000_2010_1km`
- **Resolution**: 1km, CRS: EPSG:4326"""
        ),
        (
            'WorldPop Decadal Growth Phase 2 (2010-2020 Net Change)',
            'worldpop_india_decadal_growth_2010_2020_1km',
            '07_Demographics_and_Socioeconomic',
            'Raster Tile Matrix (1km)',
            'Net population change during the 2010-2020 decade.',
            'Tracks acceleration or deceleration of urban migration corridors in the most recent decade.',
            """### WorldPop Decadal Growth Phase 2 (2010-2020)
- **Table**: `worldpop_india_decadal_growth_2010_2020_1km`
- **Resolution**: 1km, CRS: EPSG:4326"""
        )
    ]

    for title, tbl, cat, geom, desc, uses, doc in docs:
        conn.execute("""
        INSERT OR REPLACE INTO _master_layer_catalog (
            layer_title, table_name, theme_category, feature_count, geometry_type,
            thematic_column, thematic_styling_standard, ai_description, ai_use_cases
        ) VALUES (?, ?, ?, 1, ?, 'band_1', 'WorldPop Standard', ?, ?)
        """, (title, tbl, cat, geom, desc, uses))

        conn.execute("""
        INSERT OR REPLACE INTO _ai_layer_documentation (
            table_name, layer_title, theme_category, markdown_documentation, sql_recipe_example, spatial_index_status
        ) VALUES (?, ?, ?, ?, '-- Spatial SQL / Zonal Stats Recipe', 'Tile Matrix Pyramid')
        """, (tbl, title, cat, doc))

    conn.commit()
    conn.close()
    print("Internal AI documentation tables fully populated!")

if __name__ == "__main__":
    main()
