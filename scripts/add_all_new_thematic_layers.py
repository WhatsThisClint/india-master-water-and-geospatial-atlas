"""
add_all_new_thematic_layers.py
Creates and styles all advanced thematic vector duplicate layers in QGIS.
"""

import socket
import struct
import json

PORT = 9877

def main():
    qgis_code = r"""
from qgis.core import (
    QgsProject, QgsVectorLayer, QgsFillSymbol, QgsLineSymbol, QgsMarkerSymbol,
    QgsCategorizedSymbolRenderer, QgsRendererCategory,
    QgsGraduatedSymbolRenderer, QgsRendererRange, QgsCoordinateReferenceSystem
)
from qgis.PyQt.QtGui import QColor
from qgis.utils import iface

project = QgsProject.instance()
root = project.layerTreeRoot()
gpkg = "F:/Antigravity/Hydrosheds and Basins/hydrosheds_consolidated_master.gpkg"
crs_4326 = QgsCoordinateReferenceSystem("EPSG:4326")

groups = {g.name(): g for g in root.findGroups()}

def add_themed_layer(table_name, layer_title, group_name, renderer, is_visible=False):
    existing = project.mapLayersByName(layer_title)
    if existing:
        for l in existing:
            project.removeMapLayer(l.id())
            
    uri = f"{gpkg}|layername={table_name}"
    vlayer = QgsVectorLayer(uri, layer_title, "ogr")
    if vlayer.isValid():
        vlayer.setCrs(crs_4326)
        vlayer.setRenderer(renderer)
        project.addMapLayer(vlayer, False)
        grp = groups.get(group_name)
        if grp:
            node = grp.addLayer(vlayer)
            node.setItemVisibilityChecked(is_visible)
        print(f"Added: {layer_title}")
        return vlayer
    else:
        print(f"Failed to load: {table_name}")
        return None

# =========================================================================
# 1. GROUNDWATER & HYDROGEOLOGY THEMATIC LAYERS
# =========================================================================
tbl_gw = "project_jalashay_qgis_demo_06_hydrography_stage_of_groundwater_"

# 1A: Continuous Extraction Stress Ratio % (sgw_dev_pe)
gw_stress_ranges = [
    (0.0, 50.0, '#15803d', '#14532d', '0.2', '< 50% (Safe / Surplus Reserve Buffer)'),
    (50.0, 70.0, '#84cc16', '#4d7c0f', '0.2', '50% - 70% (Safe / Sustainable Draft)'),
    (70.0, 90.0, '#eab308', '#a16207', '0.25', '70% - 90% (Semi-Critical Watch Zone)'),
    (90.0, 100.0, '#f97316', '#c2410c', '0.25', '90% - 100% (Critical Extraction Threshold)'),
    (100.0, 150.0, '#dc2626', '#991b1b', '0.3', '100% - 150% (Over-Exploited / Depletion)'),
    (150.0, 500.0, '#7f1d1d', '#450a0a', '0.35', '> 150% (Severe Hyper-Exploitation Hotspot)'),
]
ranges_gw_stress = []
for min_v, max_v, fill, stroke, w, lbl in gw_stress_ranges:
    sym = QgsFillSymbol.createSimple({'color': fill, 'color_border': stroke, 'width_border': w, 'style': 'solid'})
    ranges_gw_stress.append(QgsRendererRange(min_v, max_v, sym, lbl))
rend_gw_stress = QgsGraduatedSymbolRenderer('sgw_dev_pe', ranges_gw_stress)
add_themed_layer(tbl_gw, "Stage of Groundwater Extraction [Theme: Extraction Stress Ratio (%)]", "04_Groundwater_and_Aquifers", rend_gw_stress)

# 1B: Agricultural Irrigation Draft Volume (agwd_irr)
irr_draft_ranges = [
    (0.0, 1000.0, '#fef08a', '#ca8a04', '0.2', '< 1,000 Ham (Low Irrigation Draft)'),
    (1000.0, 5000.0, '#fed7aa', '#ea580c', '0.2', '1,000 - 5,000 Ham (Moderate Irrigation Draft)'),
    (5000.0, 15000.0, '#f97316', '#c2410c', '0.25', '5,000 - 15,000 Ham (Heavy Irrigation Draft)'),
    (15000.0, 60000.0, '#b91c1c', '#450a0a', '0.35', '> 15,000 Ham (Intensive Agricultural Tube-Well Pumping)'),
]
ranges_irr_draft = []
for min_v, max_v, fill, stroke, w, lbl in irr_draft_ranges:
    sym = QgsFillSymbol.createSimple({'color': fill, 'color_border': stroke, 'width_border': w, 'style': 'solid'})
    ranges_irr_draft.append(QgsRendererRange(min_v, max_v, sym, lbl))
rend_irr_draft = QgsGraduatedSymbolRenderer('agwd_irr', ranges_irr_draft)
add_themed_layer(tbl_gw, "Stage of Groundwater Extraction [Theme: Agricultural Irrigation Draft (Ham)]", "04_Groundwater_and_Aquifers", rend_irr_draft)

# 1C: Domestic & Industrial Water Draft (agwd_dom_i)
dom_draft_ranges = [
    (0.0, 100.0, '#e0f2fe', '#0284c7', '0.2', '< 100 Ham (Rural Domestic Draft)'),
    (100.0, 500.0, '#7dd3fc', '#0369a1', '0.2', '100 - 500 Ham (Town Domestic Water Demand)'),
    (500.0, 1500.0, '#0284c7', '#075985', '0.25', '500 - 1,500 Ham (Major Urban & Industrial Demand)'),
    (1500.0, 10000.0, '#1e3a8a', '#0f172a', '0.35', '> 1,500 Ham (Megacity Industrial Water Draft)'),
]
ranges_dom_draft = []
for min_v, max_v, fill, stroke, w, lbl in dom_draft_ranges:
    sym = QgsFillSymbol.createSimple({'color': fill, 'color_border': stroke, 'width_border': w, 'style': 'solid'})
    ranges_dom_draft.append(QgsRendererRange(min_v, max_v, sym, lbl))
rend_dom_draft = QgsGraduatedSymbolRenderer('agwd_dom_i', ranges_dom_draft)
add_themed_layer(tbl_gw, "Stage of Groundwater Extraction [Theme: Domestic & Industrial Water Draft (Ham)]", "04_Groundwater_and_Aquifers", rend_dom_draft)

# 1D: Principal Aquifers Stratigraphic Geological Age (Age)
tbl_aq = "project_jalashay_qgis_demo_aquifers_aquifers"
age_map = [
    ('Quaternary', '#fef08a', '#ca8a04', 'Quaternary (Recent Alluvium & Coastal Sediments)'),
    ('Mesozoic to Cenozoic', '#fde047', '#a16207', 'Mesozoic to Cenozoic (Deccan Basalts & Sandstones)'),
    ('Paleozoic', '#a78bfa', '#5b21b6', 'Paleozoic (Gondwana Coal Basins)'),
    ('Proterozoic', '#fb923c', '#c2410c', 'Proterozoic (Vindhyan & Cuddapah Sediments)'),
    ('Azoic to Proterozoic', '#f472b6', '#9d174d', 'Azoic to Proterozoic (Dharwar & Schist Belts)'),
    ('Azoic', '#fb7185', '#881337', 'Azoic / Archean (Ancient Granite-Gneiss Basement Complex)'),
]
age_cats = []
for val, fill, stroke, lbl in age_map:
    sym = QgsFillSymbol.createSimple({'color': fill, 'color_border': stroke, 'width_border': '0.3', 'style': 'solid'})
    age_cats.append(QgsRendererCategory(val, sym, lbl))
age_cats.append(QgsRendererCategory('', QgsFillSymbol.createSimple({'color': '#cbd5e1'}), 'Unclassified Geological Age'))
rend_age = QgsCategorizedSymbolRenderer('Age', age_cats)
add_themed_layer(tbl_aq, "Principal Aquifers [Theme: Stratigraphic Geological Age]", "04_Groundwater_and_Aquifers", rend_age)

# =========================================================================
# 2. RIVER NETWORK DYNAMICS (UPLAND_SKM & DIST_DN_KM)
# =========================================================================
tbl_riv = "hydrorivers_asia_india"

# 2A: Cumulative Upstream Drainage Basin Area (UPLAND_SKM)
upland_ranges = [
    (0.0, 100.0, '#bae6fd', '0.25', '< 100 km² (Micro-Catchment Creeks)'),
    (100.0, 1000.0, '#38bdf8', '0.45', '100 - 1,000 km² (Secondary Tributaries)'),
    (1000.0, 10000.0, '#0284c7', '0.80', '1,000 - 10,000 km² (Sub-Basin Rivers)'),
    (10000.0, 100000.0, '#1d4ed8', '1.45', '10,000 - 100,000 km² (Major River Basins)'),
    (100000.0, 1200000.0, '#1e1b4b', '2.50', '> 100,000 km² (Continental Trunk Rivers: Ganga, Brahmaputra, Indus)'),
]
ranges_upland = []
for min_v, max_v, col, w, lbl in upland_ranges:
    sym = QgsLineSymbol.createSimple({'color': col, 'width': w, 'line_style': 'solid'})
    ranges_upland.append(QgsRendererRange(min_v, max_v, sym, lbl))
rend_upland = QgsGraduatedSymbolRenderer('UPLAND_SKM', ranges_upland)
add_themed_layer(tbl_riv, "HydroRIVERS Network [Theme: Cumulative Upstream Drainage Basin Area (km²)]", "03_HydroRIVERS_Network", rend_upland)

# 2B: Distance to Ocean River Mouth (DIST_DN_KM)
dist_ranges = [
    (0.0, 250.0, '#0284c7', '1.6', '0 - 250 km (Coastal Estuarine Reach)'),
    (250.0, 750.0, '#06b6d4', '1.2', '250 - 750 km (Lower Basin Reach)'),
    (750.0, 1500.0, '#eab308', '0.8', '750 - 1,500 km (Midland River Reach)'),
    (1500.0, 2500.0, '#f97316', '0.5', '1,500 - 2,500 km (Upper Basin Reach)'),
    (2500.0, 3500.0, '#dc2626', '0.35', '> 2,500 km (Distant Headwaters: Tibetan & Himalayan Sources)'),
]
ranges_dist = []
for min_v, max_v, col, w, lbl in dist_ranges:
    sym = QgsLineSymbol.createSimple({'color': col, 'width': w, 'line_style': 'solid'})
    ranges_dist.append(QgsRendererRange(min_v, max_v, sym, lbl))
rend_dist = QgsGraduatedSymbolRenderer('DIST_DN_KM', ranges_dist)
add_themed_layer(tbl_riv, "HydroRIVERS Network [Theme: Distance to Ocean Outlet (km)]", "03_HydroRIVERS_Network", rend_dist)

# =========================================================================
# 3. LAKES & WATER BODIES (ELEVATION & RESIDENCE TIME)
# =========================================================================
tbl_lake = "hydrolakes_asia_india"

# 3A: Altimetric Elevation Zones (Elevation)
elev_ranges = [
    (0.0, 100.0, '#06b6d4', '#0891b2', '0.2', '< 100 m (Coastal & Deltaic Lagoons: Chilika, Pulicat, Vembanad)'),
    (100.0, 500.0, '#2563eb', '#1d4ed8', '0.25', '100 - 500 m (Lowland Plains & River Valley Reservoirs)'),
    (500.0, 1500.0, '#6366f1', '#4338ca', '0.3', '500 - 1,500 m (Peninsular Deccan Plateau Storage Dams)'),
    (1500.0, 3500.0, '#a855f7', '#7e22ce', '0.35', '1,500 - 3,500 m (Western Ghats & Sub-Himalayan Lakes)'),
    (3500.0, 6000.0, '#38bdf8', '#0284c7', '0.45', '> 3,500 m (High Alpine Glacial Lakes: Pangong, Tso Moriri)'),
]
ranges_elev = []
for min_v, max_v, fill, stroke, w, lbl in elev_ranges:
    sym = QgsFillSymbol.createSimple({'color': fill, 'color_border': stroke, 'width_border': w, 'style': 'solid'})
    ranges_elev.append(QgsRendererRange(min_v, max_v, sym, lbl))
rend_elev = QgsGraduatedSymbolRenderer('Elevation', ranges_elev)
add_themed_layer(tbl_lake, "HydroLAKES [Theme: Elevation & Altitude Zones (m ASL)]", "06_Infrastructure_and_Projects", rend_elev)

# 3B: Water Residence & Flushing Time (Res_time in Days)
res_ranges = [
    (0.0, 30.0, '#a7f3d0', '#059669', '0.2', '< 30 Days (Fast Flushing Run-of-River Barrages)'),
    (30.0, 180.0, '#6ee7b7', '#047857', '0.25', '30 - 180 Days (Seasonal Turnover Reservoirs)'),
    (180.0, 365.0, '#38bdf8', '#0284c7', '0.3', '180 - 365 Days (Annual Carryover Storage Dams)'),
    (365.0, 3650.0, '#1d4ed8', '#1e40af', '0.4', '1 - 10 Years (Multi-Year Mega Storage Reservoirs)'),
    (3650.0, 150000.0, '#1e1b4b', '#0f172a', '0.5', '> 10 Years (Deep Endorheic / Glacial Retention Lakes)'),
]
ranges_res = []
for min_v, max_v, fill, stroke, w, lbl in res_ranges:
    sym = QgsFillSymbol.createSimple({'color': fill, 'color_border': stroke, 'width_border': w, 'style': 'solid'})
    ranges_res.append(QgsRendererRange(min_v, max_v, sym, lbl))
rend_res = QgsGraduatedSymbolRenderer('Res_time', ranges_res)
add_themed_layer(tbl_lake, "HydroLAKES [Theme: Water Residence & Flushing Time (Days)]", "06_Infrastructure_and_Projects", rend_res)

# =========================================================================
# 4. AGRICULTURE & RURAL SOCIOECONOMICS
# =========================================================================
tbl_vil = "project_jalashay_qgis_demo_01_admin_and_portfolio_india_village"

# 4A: Monsoon Kharif Crop Drought Resilience (Kharif_res)
kharif_map = [
    ('Very high', '#15803d', '#14532d', 'Very High Monsoon Kharif Resilience'),
    ('High', '#22c55e', '#166534', 'High Monsoon Kharif Resilience'),
    ('Moderate', '#eab308', '#854d0e', 'Moderate Monsoon Kharif Resilience'),
    ('Low', '#f97316', '#9a3412', 'Low Monsoon Kharif Resilience'),
    ('Very low', '#dc2626', '#7f1d1d', 'Very Low Kharif Resilience (High Drought Risk)'),
    ('NA', '#94a3b8', '#475569', 'No Data / Forest / Non-Arable'),
]
kharif_cats = []
for val, fill, stroke, lbl in kharif_map:
    sym = QgsFillSymbol.createSimple({'color': fill, 'color_border': stroke, 'width_border': '0.2', 'style': 'solid'})
    kharif_cats.append(QgsRendererCategory(val, sym, lbl))
rend_kharif = QgsCategorizedSymbolRenderer('Kharif_res', kharif_cats)
add_themed_layer(tbl_vil, "Revenue Villages [Theme: Monsoon Kharif Drought Resilience]", "01_Administrative_Boundaries", rend_kharif)

# 4B: Gram Panchayat Agricultural Development Index (ADI 2019)
tbl_gp = "project_jalashay_qgis_demo_01_admin_and_portfolio_panchayat_bou"
adi_ranges = [
    (0.0, 7.0, '#dc2626', '#7f1d1d', '0.15', '< 7.0 (Low Agricultural Development)'),
    (7.0, 9.0, '#f97316', '#9a3412', '0.15', '7.0 - 9.0 (Developing Agricultural Infrastructure)'),
    (9.0, 11.0, '#eab308', '#854d0e', '0.15', '9.0 - 11.0 (Moderate Agricultural Development)'),
    (11.0, 13.0, '#84cc16', '#3f6212', '0.2', '11.0 - 13.0 (High Agricultural Development)'),
    (13.0, 20.0, '#15803d', '#14532d', '0.25', '> 13.0 (Advanced Agrarian Infrastructure)'),
]
ranges_adi = []
for min_v, max_v, fill, stroke, w, lbl in adi_ranges:
    sym = QgsFillSymbol.createSimple({'color': fill, 'color_border': stroke, 'width_border': w, 'style': 'solid'})
    ranges_adi.append(QgsRendererRange(min_v, max_v, sym, lbl))
rend_adi = QgsGraduatedSymbolRenderer('"ADI 2019"', ranges_adi)
add_themed_layer(tbl_gp, "Gram Panchayats [Theme: Agricultural Development Index 2019 (ADI)]", "01_Administrative_Boundaries", rend_adi)

# 4C: Gram Panchayat Rural Sex Ratio (Females per 1000 Males)
sex_ratio_ranges = [
    (0.0, 850.0, '#dc2626', '#7f1d1d', '0.15', '< 850 (Severe Gender Deficit)'),
    (850.0, 920.0, '#f97316', '#9a3412', '0.15', '850 - 920 (Low Sex Ratio)'),
    (920.0, 960.0, '#eab308', '#854d0e', '0.15', '920 - 960 (Moderate Sex Ratio)'),
    (960.0, 1000.0, '#84cc16', '#3f6212', '0.2', '960 - 1,000 (Balanced Sex Ratio)'),
    (1000.0, 2000.0, '#15803d', '#14532d', '0.25', '> 1,000 (Favorable Female-to-Male Ratio)'),
]
ranges_sr = []
for min_v, max_v, fill, stroke, w, lbl in sex_ratio_ranges:
    sym = QgsFillSymbol.createSimple({'color': fill, 'color_border': stroke, 'width_border': w, 'style': 'solid'})
    ranges_sr.append(QgsRendererRange(min_v, max_v, sym, lbl))
rend_sr = QgsGraduatedSymbolRenderer('("Total_Fema" / NULLIF("Total_Male", 0)) * 1000', ranges_sr)
add_themed_layer(tbl_gp, "Gram Panchayats [Theme: Rural Sex Ratio (Females per 1000 Males)]", "01_Administrative_Boundaries", rend_sr)

# =========================================================================
# 5. POWER & TRANSMISSION GRID
# =========================================================================
tbl_util = "overture_utility_infrastructure"
power_cats = [
    ('power_tower', '#dc2626', '0.7', 'High-Voltage Electrical Power Towers'),
    ('generator', '#f97316', '0.6', 'Power Generation Plants & Substations'),
    ('bridge', '#3b82f6', '0.5', 'Transport & Pipeline Bridges'),
    ('breakwater', '#06b6d4', '0.5', 'Maritime Breakwaters & Sea Barriers'),
]
power_renderer_cats = []
for val, col, w, lbl in power_cats:
    sym = QgsLineSymbol.createSimple({'color': col, 'width': w, 'line_style': 'solid'})
    power_renderer_cats.append(QgsRendererCategory(val, sym, lbl))
power_renderer_cats.append(QgsRendererCategory('', QgsLineSymbol.createSimple({'color': '#94a3b8', 'width': '0.3'}), 'Other Utility Infrastructure'))
rend_power = QgsCategorizedSymbolRenderer('class', power_renderer_cats)
add_themed_layer(tbl_util, "Overture Infrastructure [Theme: Power Grid & Transmission Towers]", "06_Infrastructure_and_Projects", rend_power)

if iface:
    iface.mapCanvas().refresh()

uri_proj = f"geopackage:{gpkg}?projectName=India_Master_Hydrology_and_Infrastructure"
saved = project.write(uri_proj)
print(f"All new thematic layers successfully saved to project: {saved}")
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
    print("New thematic layers added and saved to project!")

if __name__ == "__main__":
    main()
