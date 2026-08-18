"""
inspect_panchayat_demographics.py
Inspects exact population distributions in Gram Panchayat Boundaries.
"""

import sqlite3
import pandas as pd

GPKG_PATH = r"F:\Antigravity\Hydrosheds and Basins\hydrosheds_consolidated_master.gpkg"

def main():
    conn = sqlite3.connect(GPKG_PATH)
    tbl = "project_jalashay_qgis_demo_01_admin_and_portfolio_panchayat_bou"

    print("=== GRAM PANCHAYAT CENSUS DEMOGRAPHICS ===")
    df_stats = pd.read_sql_query(f'SELECT count(*) as total_records, count(CASE WHEN Total_Popu > 0 THEN 1 END) as with_pop, min(Total_Popu) as min_pop, max(Total_Popu) as max_pop, avg(Total_Popu) as avg_pop FROM "{tbl}"', conn)
    print(df_stats.to_string())

    print("\n=== SAMPLE ROWS ===")
    df_sample = pd.read_sql_query(f'SELECT "Total_Popu", "Total_Male", "Female_Lit", "Male_Liter", "Female_SC_", "Female_ST_" FROM "{tbl}" WHERE "Total_Popu" > 0 LIMIT 10', conn)
    print(df_sample.to_string())

    conn.close()

if __name__ == "__main__":
    main()
