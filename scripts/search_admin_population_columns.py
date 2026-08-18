"""
search_admin_population_columns.py
Searches all administrative vector tables in the GeoPackage for population columns.
"""

import sqlite3
import pandas as pd

GPKG_PATH = r"F:\Antigravity\Hydrosheds and Basins\hydrosheds_consolidated_master.gpkg"

ADMIN_TABLES = [
    "project_jalashay_qgis_demo_01_admin_and_portfolio_state_boundar",
    "project_jalashay_qgis_demo_01_admin_and_portfolio_district_boun",
    "project_jalashay_qgis_demo_01_admin_and_portfolio_panchayat_bou",
    "project_jalashay_qgis_demo_01_admin_and_portfolio_india_village",
    "parliamentary_constituencies_lok_sabha",
    "assembly_constituencies_vidhan_sabha",
    "overture_administrative_divisions",
    "geopackage_data_india_geoportal_layers_india_populated_places",
    "project_jalashay_qgis_demo_06_hydrography_stage_of_groundwater_"
]

def main():
    conn = sqlite3.connect(GPKG_PATH)
    print("=== SEARCHING ADMINISTRATIVE TABLES FOR POPULATION COLUMNS ===\n")
    
    for tbl in ADMIN_TABLES:
        cols = [c[1] for c in conn.execute(f'PRAGMA table_info("{tbl}")').fetchall()]
        print(f"Table: {tbl}")
        
        # Check all column names
        pop_cols = [c for c in cols if any(k in c.lower() for k in ['pop', 'tot_p', 'p_', 'census', 'inhab', 'elect', 'voter', 'hh', 'house', 'male', 'female'])]
        if pop_cols:
            print(f"  Candidate population columns ({len(pop_cols)}): {pop_cols}")
            for pc in pop_cols:
                sample = conn.execute(f'SELECT DISTINCT "{pc}" FROM "{tbl}" WHERE "{pc}" IS NOT NULL AND "{pc}" != "" LIMIT 5').fetchall()
                vals = [s[0] for s in sample]
                print(f"    - {pc}: {vals}")
        else:
            print("  No obvious population columns by name. Listing all columns:")
            print(f"    {cols}")
        print()

    conn.close()

if __name__ == "__main__":
    main()
