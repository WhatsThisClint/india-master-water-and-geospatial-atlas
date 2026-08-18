# India Master Water & Geospatial Atlas 🌊🗺️

[![Direct Download GeoPackage (1.57 GB)](https://img.shields.io/badge/Download-GeoPackage%20(1.57%20GB)-2563eb?style=for-the-badge&logo=googlecloudstorage&logoColor=white)](https://github.com/WhatsThisClint/india-master-water-and-geospatial-atlas/releases/download/v1.0.1/india_master_water_and_geospatial_atlas.zip)

[![OGC GeoPackage](https://img.shields.io/badge/OGC-GeoPackage%201.2-blue.svg)](https://www.geopackage.org/)
[![CRS EPSG:4326](https://img.shields.io/badge/CRS-EPSG%3A4326%20WGS84-brightgreen.svg)](https://epsg.io/4326)
[![Layers 75](https://img.shields.io/badge/Active%20Layers-75%20Layers-orange.svg)](#thematic-architecture)
[![QGIS Ready](https://img.shields.io/badge/QGIS-3.28%2B%20%7C%203.34%20LTR-93b023.svg)](https://qgis.org/)
[![GitHub Release](https://img.shields.io/github/v/release/WhatsThisClint/india-master-water-and-geospatial-atlas)](https://github.com/WhatsThisClint/india-master-water-and-geospatial-atlas/releases)

An authoritative, enterprise-grade, consolidated All-India Hydrological, Hydrogeological, Demographic, Administrative, and Infrastructure Master Spatial Intelligence Geodatabase.

---

## ⚡ Direct Download

You can download the full consolidated database directly from the GitHub Release asset:

📥 **[Download Master GeoPackage Archive (`india_master_water_and_geospatial_atlas.zip` — 1.57 GB)](https://github.com/WhatsThisClint/india-master-water-and-geospatial-atlas/releases/download/v1.0.1/india_master_water_and_geospatial_atlas.zip)**

*After unzipping, the file extracts to `india_master_water_and_geospatial_atlas.gpkg` (3.62 GB).*

---

## 🌟 Key Highlights

- **Consolidated Single-File Database**: All 75 production layers, raster grids, and internal metadata tables are stored in a single optimized **3.62 GB** OGC GeoPackage (`india_master_water_and_geospatial_atlas.gpkg`), recovering **13.66 GB** through zero-copy multi-thematic views.
- **100% Unified Spatial Reference System**: Every single vector polygon, river reach, boundary, and raster cell is native **`EPSG:4326 (WGS 84)`** with 0 projection distortion.
- **Zero-Storage Multi-Thematic Views**: 27 specialized visual layers (e.g. Transmissivity, Continuous Groundwater Extraction Stress %, Rural Literacy, 20-Year Net Urbanization) created as duplicate views pointing to parent SQLite tables with zero disk footprint.
- **Multi-Decadal Gridded Demographics**: Full WorldPop 2000, 2010, 2020, and 20-Year Net Growth grids embedded as native OGC GeoPackage raster tile pyramids.
- **Built-in AI & Spatial Metadata**: Complete encyclopedic attribute dictionary covering **703 columns** with physical units and analytical guides embedded in SQLite tables.
- **Embedded QGIS Project**: The entire styled workspace is embedded directly inside the database as `India_Master_Hydrology_and_Infrastructure`.

---

## 📂 Thematic Architecture (75 Layers Across 7 Groups)

```
india_master_water_and_geospatial_atlas.gpkg
├── 01_Administrative_Boundaries (11 Layers)
│   ├── India National Boundary
│   ├── State & UT Boundaries (36 States/UTs)
│   ├── District Boundaries (666 Districts)
│   ├── Lok Sabha Parliamentary Constituencies (2019)
│   ├── Vidhan Sabha State Assembly Constituencies (4,182 ACs)
│   ├── Gram Panchayat Boundaries (209k Panchayats: Population, Literacy, ADI, Sex Ratio)
│   ├── Revenue Village Boundaries (653k Villages: Crop Area, Kharif/Rabi Drought Resilience)
│   └── Overture Administrative Boundaries (63k Boundaries)
├── 02_HydroBASINS_Hierarchy (12 Layers: Levels 12 ➔ 1)
│   └── Continental Basins (L1) down to Microwatersheds (L12)
├── 03_HydroRIVERS_Network (11 Layers)
│   ├── HydroRIVERS Stream Network (261k Reaches)
│   ├── Themes: Discharge (m³/s), Cumulative Basin Area (km²), Distance to Ocean (km)
│   └── River Orders 1 through 8 (Headwater Creeks to Mega Estuaries)
├── 04_Groundwater_and_Aquifers (10 Layers)
│   ├── Stage of Groundwater Extraction (7,274 Blocks: Stress %, Irrigation/Domestic Draft)
│   └── CGWB Principal Aquifers (518 Formations: Transmissivity, Specific Yield, Age, Well Yield)
├── 05_Geology_and_Lithology (2 Layers)
│   └── GLiM India Geological Formations & Permeability Classifications (15,726 Polygons)
├── 06_Infrastructure_and_Projects (9 Layers)
│   ├── HydroLAKES Lakes & Reservoirs (11,221 Water Bodies: Storage MCM, Elevation, Flushing Days)
│   ├── Major Populated Places & Cities (348 Cities: 100-Year 1950-2050 Demographic Projections)
│   ├── Major Ports & Harbours (1,081 Ports)
│   ├── Overture Utility & Power Infrastructure (2.62 Million Transmission Towers & Substations)
│   └── India WRIS Water Resources Hydro Projects (303 Facilities)
└── 07_Demographics_and_Socioeconomic (10 Raster Tile Sets)
    ├── WorldPop 20-Year Net Population Growth (2000-2020)
    ├── WorldPop 20-Year Percentage Population Growth (% Change)
    ├── WorldPop Decadal Growth Phases (2000-2010 & 2010-2020)
    ├── WorldPop 2020 Settlement Typology (Rural to Megacity)
    └── WorldPop India 2000, 2010, 2020 Population Count & Density
```

---

## 📖 Detailed Documentation

| Document | Description |
| :--- | :--- |
| **[`docs/SCHEMA_AND_LAYER_CATALOG.md`](docs/SCHEMA_AND_LAYER_CATALOG.md)** | Complete layer inventory, table names, feature counts, and styling presets. |
| **[`docs/ATTRIBUTE_DICTIONARY.md`](docs/ATTRIBUTE_DICTIONARY.md)** | Comprehensive dictionary covering 703 attribute columns with units and AI guides. |
| **[`docs/SPATIAL_ANALYTICS_COOKBOOK.md`](docs/SPATIAL_ANALYTICS_COOKBOOK.md)** | Production Spatial SQL recipes, zonal statistics scripts, and hydrogeological queries. |
| **[`docs/PYQGIS_AUTOMATION_GUIDE.md`](docs/PYQGIS_AUTOMATION_GUIDE.md)** | Headless automation, high-resolution map generation, and QGIS socket control. |
| **[`CHANGELOG.md`](CHANGELOG.md)** | Full history of releases, added layers, and structural migrations. |

---

## 🚀 Quick Start Guide

### Interactive Usage in QGIS
1. Launch QGIS (3.28 LTR or 3.34+).
2. Go to **Project $\\rightarrow$ Open From $\\rightarrow$ GeoPackage...**
3. Select `india_master_water_and_geospatial_atlas.gpkg`.
4. Choose the project **`India_Master_Hydrology_and_Infrastructure`**.

### Spatial SQL via GDAL / SQLite
```bash
# Query population living in Over-Exploited groundwater blocks
ogrinfo india_master_water_and_geospatial_atlas.gpkg -sql "
  SELECT district, state, sgw_dev_pe, agwd_irr 
  FROM project_jalashay_qgis_demo_06_hydrography_stage_of_groundwater_ 
  WHERE class = 'Over-Exploited' 
  ORDER BY sgw_dev_pe DESC LIMIT 10
"
```

---

## 📚 Citation & DOI

If you utilize this geospatial database, layers, documentation, or analytical workflows in your research, publications, or engineering models, please cite it using the repository's native `CITATION.cff` or the following format:

### APA Format
> Fernandes, C. (2026). *India Master Water & Geospatial Atlas: A Consolidated 75-Layer Hydrological, Hydrogeological, Demographic, and Infrastructure Geodatabase* (Version 1.0.1) [Spatial Database]. GitHub. https://github.com/WhatsThisClint/india-master-water-and-geospatial-atlas

### BibTeX
```bibtex
@software{fernandes_india_master_atlas_2026,
  author       = {Clinton Fernandes},
  title        = {{India Master Water & Geospatial Atlas: A Consolidated 75-Layer Hydrological, Hydrogeological, Demographic, and Infrastructure Geodatabase}},
  year         = {2026},
  version      = {1.0.1},
  publisher    = {GitHub},
  url          = {https://github.com/WhatsThisClint/india-master-water-and-geospatial-atlas}
}
```

---

## 🛠️ Tech Stack & Compliance

- **Format**: OGC GeoPackage 1.2 / SQLite 3
- **Raster Tile Architecture**: OGC `gpkg_tile_matrix` pyramids (Zoom levels 0 to 4)
- **Coordinate Reference System**: `EPSG:4326 - WGS 84` (Latitude / Longitude)
- **Compatibility**: QGIS, ArcGIS Pro, GDAL, GeoPandas, PostGIS, MapLibre, DuckDB Spatial
"""
    with open(os.path.join(REPO_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)
    print("README.md updated with Direct Download badge!")
