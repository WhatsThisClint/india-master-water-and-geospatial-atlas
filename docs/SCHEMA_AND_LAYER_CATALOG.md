# India Master Water & Geospatial Atlas — Complete Layer Catalog

> **Total Active Production Layers**: **75 Layers**
> **Coordinate Reference System**: `EPSG:4326 (WGS 84)` across 100% of layers

---


## Group `01_Administrative_Boundaries`

| Layer Title | Underlying Table | Count | Geometry | Thematic Key | Symbology / Styling | Description |
| :--- | :--- | :---: | :---: | :--- | :--- | :--- |
| **`District Boundaries (All India - 734 Districts)`** | `project_jalashay_qgis_demo_01_admin_and_portfolio_district_boun` | 666 | `MULTIPOLYGON` | `Name` | Custom / Natural Earth | Complete nationwide district administrative boundaries. |
| **`India National Boundary`** | `india_boundary_indian_boundary` | 1 | `MULTIPOLYGON` | `None` | Custom / Natural Earth | Single outline defining the sovereign land territory and international borders of India. |
| **`Lok Sabha Parliamentary Constituencies (2019)`** | `parliamentary_constituencies_lok_sabha` | 543 | `MULTIPOLYGON` | `pc_category` | Election Commission of India | 543 national parliamentary constituencies classified by reservation status (GEN, SC, ST). |
| **`Overture Administrative Divisions (India)`** | `overture_administrative_divisions` | 63,261 | `GEOMETRY` | `subtype` | Overture Maps Standard | Open global administrative division polygons categorized into regions, counties, localities, and neighborhoods. |
| **`State & UT Boundaries (All India)`** | `project_jalashay_qgis_demo_01_admin_and_portfolio_state_boundar` | 36 | `MULTIPOLYGON` | `Name` | Custom / Natural Earth | 36 States and Union Territories of India with administrative boundaries. |
| **`Vidhan Sabha State Assembly Constituencies`** | `assembly_constituencies_vidhan_sabha` | 4,182 | `MULTIPOLYGON` | `ST_NAME` | Custom / Natural Earth | 4,182 state legislative assembly constituencies across India. |
| **`Revenue Villages [Theme: Monsoon Kharif Drought Resilience]`** | `project_jalashay_qgis_demo_01_admin_and_portfolio_india_village` | 653,582 | `MULTIPOLYGON` | `Kharif_res` | Categorized Green-to-Red Resilience | Monsoon Kharif season agricultural drought resilience classification (Very High to Very Low). |
| **`Gram Panchayats [Theme: Rural Sex Ratio (Females per 1000 Males)]`** | `project_jalashay_qgis_demo_01_admin_and_portfolio_panchayat_bou` | 209,151 | `MULTIPOLYGON` | `Total_Fema/Total_Male` | Graduated Demographic Balance Ramp | Demographic sex ratio (Females per 1,000 Males) calculated from official Census counts. |

## Group `02_HydroBASINS_Hierarchy`

| Layer Title | Underlying Table | Count | Geometry | Thematic Key | Symbology / Styling | Description |
| :--- | :--- | :---: | :---: | :--- | :--- | :--- |
| **`HydroBASINS Level 1 (Continental Basins)`** | `hydrobasins_asia_level_1` | 1 | `MULTIPOLYGON` | `SUB_AREA` | HydroSHEDS / Pfafstetter Topological Hierarchy | 1 South Asia continental drainage basin envelope. |
| **`HydroBASINS Level 10 (Micro-catchments)`** | `hydrobasins_asia_level_10` | 23,626 | `MULTIPOLYGON` | `SUB_AREA` | HydroSHEDS / Pfafstetter Topological Hierarchy | 23,626 micro-catchment hydrological units. |
| **`HydroBASINS Level 11 (Sub-microwatersheds)`** | `hydrobasins_asia_level_11` | 25,684 | `MULTIPOLYGON` | `SUB_AREA` | HydroSHEDS / Pfafstetter Topological Hierarchy | 25,684 sub-microwatersheds. |
| **`HydroBASINS Level 12 (Microwatersheds)`** | `hydrobasins_asia_level_12` | 25,737 | `MULTIPOLYGON` | `SUB_AREA` | HydroSHEDS / Pfafstetter Topological Hierarchy | 25,737 finest microwatersheds in India (~10-50 sq km). |
| **`HydroBASINS Level 2 (Major Regional Basins)`** | `hydrobasins_asia_level_2` | 4 | `MULTIPOLYGON` | `SUB_AREA` | HydroSHEDS / Pfafstetter Topological Hierarchy | 4 continental-scale drainage regions across South Asia. |
| **`HydroBASINS Level 3 (Basin Systems)`** | `hydrobasins_asia_level_3` | 10 | `MULTIPOLYGON` | `SUB_AREA` | HydroSHEDS / Pfafstetter Topological Hierarchy | 10 primary river basin systems (Ganga, Indus, Brahmaputra, Godavari, Krishna, etc.). |
| **`HydroBASINS Level 4 (Sub-basin Systems)`** | `hydrobasins_asia_level_4` | 37 | `MULTIPOLYGON` | `SUB_AREA` | HydroSHEDS / Pfafstetter Topological Hierarchy | 37 major sub-basin systems. |
| **`HydroBASINS Level 5 (Watersheds)`** | `hydrobasins_asia_level_5` | 124 | `MULTIPOLYGON` | `SUB_AREA` | HydroSHEDS / Pfafstetter Topological Hierarchy | 124 major watersheds. |
| **`HydroBASINS Level 6 (Sub-watersheds)`** | `hydrobasins_asia_level_6` | 443 | `MULTIPOLYGON` | `SUB_AREA` | HydroSHEDS / Pfafstetter Topological Hierarchy | 443 sub-watersheds. |
| **`HydroBASINS Level 7 (Drainage Catchments)`** | `hydrobasins_asia_level_7` | 1,518 | `MULTIPOLYGON` | `SUB_AREA` | HydroSHEDS / Pfafstetter Topological Hierarchy | 1,518 medium drainage catchments. |
| **`HydroBASINS Level 8 (Catchments)`** | `hydrobasins_asia_level_8` | 4,797 | `MULTIPOLYGON` | `SUB_AREA` | HydroSHEDS / Pfafstetter Topological Hierarchy | 4,797 standard catchment units. |
| **`HydroBASINS Level 9 (Sub-catchments)`** | `hydrobasins_asia_level_9` | 12,773 | `MULTIPOLYGON` | `SUB_AREA` | HydroSHEDS / Pfafstetter Topological Hierarchy | 12,773 sub-catchments. |

## Group `03_HydroRIVERS_Network`

| Layer Title | Underlying Table | Count | Geometry | Thematic Key | Symbology / Styling | Description |
| :--- | :--- | :---: | :---: | :--- | :--- | :--- |
| **`HydroRIVERS Order 1 (Headwater Streams)`** | `hydrorivers_india_order_1` | 134,053 | `MULTILINESTRING` | `ORD_STRA` | HydroSHEDS / Strahler Stream Order | 134,053 headwater streams. Width: 0.20mm. |
| **`HydroRIVERS Order 2 (Secondary Streams)`** | `hydrorivers_india_order_2` | 59,274 | `MULTILINESTRING` | `ORD_STRA` | HydroSHEDS / Strahler Stream Order | 59,274 secondary streams. Width: 0.35mm. |
| **`HydroRIVERS Order 3 (Tertiary Streams)`** | `hydrorivers_india_order_3` | 32,518 | `MULTILINESTRING` | `ORD_STRA` | HydroSHEDS / Strahler Stream Order | 32,518 tertiary streams. Width: 0.50mm. |
| **`HydroRIVERS Order 4 (Sub-Rivers)`** | `hydrorivers_india_order_4` | 18,845 | `MULTILINESTRING` | `ORD_STRA` | HydroSHEDS / Strahler Stream Order | 18,845 sub-river streams. Width: 0.70mm. |
| **`HydroRIVERS Order 5 (Medium Rivers)`** | `hydrorivers_india_order_5` | 9,497 | `MULTILINESTRING` | `ORD_STRA` | HydroSHEDS / Strahler Stream Order | 9,497 medium river reaches. Width: 0.95mm. |
| **`HydroRIVERS Order 6 (Major Rivers)`** | `hydrorivers_india_order_6` | 4,570 | `MULTILINESTRING` | `ORD_STRA` | HydroSHEDS / Strahler Stream Order | 4,570 major river reaches (Yamuna, Cauvery, Tapi, Chambal). Width: 1.30mm. |
| **`HydroRIVERS Order 7 (Large Trunk Rivers)`** | `hydrorivers_india_order_7` | 1,580 | `MULTILINESTRING` | `ORD_STRA` | HydroSHEDS / Strahler Stream Order | Major trunk rivers (Ganga, Godavari, Krishna, Narmada, Mahanadi mainstems). Width: 1.70mm. |
| **`HydroRIVERS Order 8 (Mega River Estuaries & Outlets)`** | `hydrorivers_india_order_8` | 1,284 | `MULTILINESTRING` | `ORD_STRA` | HydroSHEDS / Strahler Stream Order | Mega river trunk mouths (Ganga, Brahmaputra delta mouths). Width: 2.40mm. |
| **`India Major Rivers Network`** | `india_geoportal_data_gis_geopackage_india_geoportal_layers_indi_1` | 94 | `MULTILINESTRING` | `name` | HydroSHEDS / Strahler Stream Order | Cartographically generalized major river centerlines with named attributes. |
| **`HydroRIVERS Network [Theme: Distance to Ocean Outlet (km)]`** | `hydrorivers_asia_india` | 261,621 | `LINESTRING` | `DIST_DN_KM` | Graduated Thermal Distance Ramp | Distance in kilometers along the river network to the final oceanic or terminal lake outlet. |

## Group `04_Groundwater_and_Aquifers`

| Layer Title | Underlying Table | Count | Geometry | Thematic Key | Symbology / Styling | Description |
| :--- | :--- | :---: | :---: | :--- | :--- | :--- |
| **`Stage of Groundwater Extraction [Theme: Domestic & Industrial Water Draft (Ham)]`** | `project_jalashay_qgis_demo_06_hydrography_stage_of_groundwater_` | 7,274 | `MULTIPOLYGON` | `agwd_dom_i` | Graduated Cyan-Blue Fill | Annual groundwater draft volume dedicated to municipal drinking water and industrial manufacturing. |
| **`Principal Aquifers [Theme: Stratigraphic Geological Age]`** | `project_jalashay_qgis_demo_aquifers_aquifers` | 518 | `MULTIPOLYGON` | `Age` | Geological Chronology Palette | Stratigraphic geological age of India principal aquifers (Quaternary, Mesozoic, Paleozoic, Proterozoic, Archean/Azoic). |

## Group `05_Geology_and_Lithology`

| Layer Title | Underlying Table | Count | Geometry | Thematic Key | Symbology / Styling | Description |
| :--- | :--- | :---: | :---: | :--- | :--- | :--- |
| **`GLiM India Lithology & Formations`** | `project_jalashay_qgis_demo_07_soils_and_geology_glim_india_lith` | 15,726 | `MULTIPOLYGON` | `lith_class` | GLiM / Hartmann & Moosdorf (2012) | 15,726 lithological rock polygons (Global Lithological Map Standard: Hartmann & Moosdorf 2012). |

## Group `06_Infrastructure_and_Projects`

| Layer Title | Underlying Table | Count | Geometry | Thematic Key | Symbology / Styling | Description |
| :--- | :--- | :---: | :---: | :--- | :--- | :--- |
| **`India WRIS Water Resources Projects`** | `geopackage_data_india_geoportal_layers_india_wris_water_project` | 303 | `GEOMETRY` | `TYPE` | Custom / Natural Earth | 303 national water resources infrastructure projects (Dams, Barrages, Lift Irrigation Schemes). |
| **`Major Populated Places & Cities`** | `geopackage_data_india_geoportal_layers_india_populated_places` | 348 | `POINT` | `featurecla` | Custom / Natural Earth | 348 urban centers and capital cities with population ranks. |
| **`Major Ports & Harbours of India`** | `geopackage_data_india_geoportal_layers_india_ports` | 1,081 | `POINT` | `PORT_TYPE` | Custom / Natural Earth | 1,081 maritime ports, harbours, and coastal terminals. |
| **`HydroLAKES [Theme: Water Residence & Flushing Time (Days)]`** | `hydrolakes_asia_india` | 11,221 | `MULTIPOLYGON` | `Res_time` | Graduated Turnover Time Ramp | Theoretical hydraulic retention time in days (how long water resides before flushing). |
| **`Overture Infrastructure [Theme: Power Grid & Transmission Towers]`** | `overture_utility_infrastructure` | 2,625,952 | `LINESTRING` | `class` | Categorized Power Grid Symbols | National electrical power grid, high-voltage transmission towers, substations, and utility corridors. |

## Group `07_Demographics_and_Socioeconomic`

| Layer Title | Underlying Table | Count | Geometry | Thematic Key | Symbology / Styling | Description |
| :--- | :--- | :---: | :---: | :--- | :--- | :--- |
| **`WorldPop India 2000 Baseline Population Count (1km)`** | `worldpop_india_2000_population_count_1km` | 1 | `Raster / Tile Matrix (1km)` | `band_1 (Persons per Pixel)` | WorldPop Historical Pseudocolor | Baseline gridded population count for India in Year 2000 (UN-Adjusted). |
| **`WorldPop India 2010 Mid-Term Population Count (1km)`** | `worldpop_india_2010_population_count_1km` | 1 | `Raster / Tile Matrix (1km)` | `band_1 (Persons per Pixel)` | WorldPop Historical Pseudocolor | Mid-term gridded population count for India in Year 2010 (UN-Adjusted). |
| **`WorldPop India 2020 Population Count (1km)`** | `worldpop_india_2020_population_count_1km` | 1 | `Raster / Tile Matrix (1km)` | `band_1 (Persons per Pixel)` | Plasma Radiant Night Glow Heatmap | Current high-resolution gridded population count for India (WorldPop 2020 UN-Adjusted). |
| **`WorldPop 20-Year Net Population Growth (2000-2020)`** | `worldpop_india_20yr_net_growth_2000_2020_1km` | 1 | `Raster Tile Matrix (1km)` | `band_1` | WorldPop Standard | Net change in human population count per 1km grid cell from 2000 to 2020 (Pop2020 - Pop2000). |
| **`WorldPop 20-Year Percentage Population Growth (% Change 2000-2020)`** | `worldpop_india_20yr_pct_growth_2000_2020_1km` | 1 | `Raster Tile Matrix (1km)` | `band_1` | WorldPop Standard | Relative percentage population growth rate from 2000 to 2020 (% Change). |
| **`WorldPop 2020 Settlement Typology (Rural to Megacity)`** | `worldpop_india_2020_population_density_1km` | 1 | `Raster Tile Matrix (1km)` | `band_1` | WorldPop Standard | Discrete human settlement classification based on population density thresholds. |
| **`WorldPop Decadal Growth Phase 1 (2000-2010 Net Change)`** | `worldpop_india_decadal_growth_2000_2010_1km` | 1 | `Raster Tile Matrix (1km)` | `band_1` | WorldPop Standard | Net population change during the 2000-2010 decade. |
| **`WorldPop Decadal Growth Phase 2 (2010-2020 Net Change)`** | `worldpop_india_decadal_growth_2010_2020_1km` | 1 | `Raster Tile Matrix (1km)` | `band_1` | WorldPop Standard | Net population change during the 2010-2020 decade. |