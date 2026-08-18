# Spatial Analytics & Hydrogeological SQL Cookbook

This guide contains production-ready Spatial SQL queries, Python automation scripts, and zonal analysis recipes for the **India Master Water & Geospatial Atlas**.

---

## 1. Groundwater Vulnerability & Population Exposure

### Query: Identify Over-Exploited Groundwater Blocks with High Rural Population
```sql
SELECT 
    gw.block,
    gw.district,
    gw.state,
    gw.sgw_dev_pe AS extraction_ratio_pct,
    gw.agwd_irr AS irrigation_draft_ham,
    gw.agwd_dom_i AS domestic_draft_ham,
    COUNT(gp.fid) AS total_panchayats,
    SUM(gp.Total_Popu) AS total_rural_population,
    SUM(gp.Female_Lit) / NULLIF(SUM(gp.Female_Lit + gp.Female_Ill), 0) * 100 AS female_literacy_rate
FROM project_jalashay_qgis_demo_06_hydrography_stage_of_groundwater_ gw
JOIN project_jalashay_qgis_demo_01_admin_and_portfolio_panchayat_bou gp
  ON ST_Intersects(gw.geom, gp.geom)
WHERE gw.class = 'Over-Exploited'
GROUP BY gw.block, gw.district, gw.state
ORDER BY total_rural_population DESC
LIMIT 50;
```

---

## 2. River Basin & Surface Water Budgeting

### Query: Cumulative Watershed Inflow & Storage Volume by Basin Level 7
```sql
SELECT 
    b.HYBAS_ID AS basin_id,
    b.SUB_AREA AS sub_basin_area_km2,
    b.UP_AREA AS cumulative_upstream_area_km2,
    COUNT(DISTINCT r.HYRIV_ID) AS river_reach_count,
    MAX(r.DIS_AV_CMS) AS peak_river_discharge_cms,
    COUNT(DISTINCT l.Hylak_id) AS total_lakes_and_reservoirs,
    SUM(l.Vol_total) AS total_lake_storage_mcm
FROM hydrobasins_asia_level_7 b
LEFT JOIN hydrorivers_asia_india r ON ST_Intersects(b.geom, r.geom)
LEFT JOIN hydrolakes_asia_india l ON ST_Intersects(b.geom, l.geom)
GROUP BY b.HYBAS_ID
ORDER BY total_lake_storage_mcm DESC;
```

---

## 3. High-Growth Urban Metros & Projected Municipal Water Demand

### Query: Top 25 Rapidly Growing Cities Facing Water Allocation Challenges
```sql
SELECT 
    NAME AS city_name,
    ADM1NAME AS state_or_province,
    LATITUDE,
    LONGITUDE,
    POP2000 AS pop_2000,
    POP2020 AS pop_2020,
    POP2050 AS projected_pop_2050,
    (POP2050 - POP2020) AS net_future_growth,
    ROUND(((POP2050 - POP2020) / NULLIF(POP2020, 0)) * 100, 1) AS growth_rate_pct
FROM geopackage_data_india_geoportal_layers_india_populated_places
WHERE POP_MAX > 500000
ORDER BY net_future_growth DESC
LIMIT 25;
```

---

## 4. Python Zonal Statistics on WorldPop Gridded Layers

```python
import rasterio
import geopandas as gpd
from rasterstats import zonal_stats

# Load administrative polygons and WorldPop raster
gdf = gpd.read_file("india_master_water_and_geospatial_atlas.gpkg", layer="project_jalashay_qgis_demo_01_admin_and_portfolio_district_boun")
raster_path = "GPKG:india_master_water_and_geospatial_atlas.gpkg:worldpop_india_2020_population_count_1km"

# Compute zonal statistics
stats = zonal_stats(gdf, raster_path, stats=["sum", "mean", "max"])
gdf["total_pop_2020"] = [s["sum"] for s in stats]

print(gdf[["Name", "total_pop_2020"]].head())
```
