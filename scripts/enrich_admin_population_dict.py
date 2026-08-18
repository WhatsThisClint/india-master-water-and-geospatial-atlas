"""
enrich_admin_population_dict.py
Updates _layer_attribute_dictionary with full definitions for all administrative population columns.
"""

import sqlite3

GPKG_PATH = r"F:\Antigravity\Hydrosheds and Basins\hydrosheds_consolidated_master.gpkg"

def main():
    conn = sqlite3.connect(GPKG_PATH)

    gp_tbl = "project_jalashay_qgis_demo_01_admin_and_portfolio_panchayat_bou"
    gp_updates = [
        ("Total_Popu", "Persons (Count)", 1, "Total human population residing within the Gram Panchayat according to the official Indian Census.", "Use for local rural drinking water demand calculation and per-capita water stress analysis."),
        ("Total_Male", "Persons (Count)", 0, "Total male population in the Gram Panchayat.", "Demographic sex structure analysis."),
        ("Female_Lit", "Persons (Count)", 1, "Number of literate females in the Gram Panchayat.", "Female literacy and socioeconomic development baseline."),
        ("Female_Ill", "Persons (Count)", 0, "Number of illiterate females in the Gram Panchayat.", "Socioeconomic vulnerability metric."),
        ("Male_Liter", "Persons (Count)", 0, "Number of literate males in the Gram Panchayat.", "Male literacy baseline."),
        ("Male_Illit", "Persons (Count)", 0, "Number of illiterate males in the Gram Panchayat.", "Socioeconomic vulnerability metric."),
        ("Female_SC_", "Persons (Count)", 0, "Scheduled Caste (SC) female population.", "Social equity and targeted welfare analysis."),
        ("Male_SC_Po", "Persons (Count)", 0, "Scheduled Caste (SC) male population.", "Social equity and targeted welfare analysis."),
        ("Female_ST_", "Persons (Count)", 0, "Scheduled Tribe (ST) female population.", "Tribal water rights and forest catchment community analysis."),
        ("Male_ST_Po", "Persons (Count)", 0, "Scheduled Tribe (ST) male population.", "Tribal water rights and forest catchment community analysis."),
    ]

    for col, unit, is_key, sem_def, ai_guide in gp_updates:
        conn.execute("""
        UPDATE _layer_attribute_dictionary
        SET unit_of_measurement = ?, is_thematic_key = ?, semantic_definition = ?, ai_interpretation_guide = ?
        WHERE table_name = ? AND column_name = ?
        """, (unit, is_key, sem_def, ai_guide, gp_tbl, col))

    city_tbl = "geopackage_data_india_geoportal_layers_india_populated_places"
    city_updates = [
        ("POP_MAX", "Persons (Count)", 1, "Maximum estimated urban agglomeration population for the city / populated place.", "Urban water consumption modeling and municipal water supply infrastructure sizing."),
        ("POP_MIN", "Persons (Count)", 0, "Minimum core municipal population count.", "Municipal core population baseline."),
        ("POP2000", "Persons (Count)", 0, "Historical city population in Year 2000.", "20-year urban growth trajectory baseline."),
        ("POP2010", "Persons (Count)", 0, "Historical city population in Year 2010.", "Decadal urban growth midpoint."),
        ("POP2020", "Persons (Count)", 1, "Estimated city population in Year 2020.", "Current urban water demand modeling."),
        ("POP2050", "Persons (Count)", 1, "Long-term projected urban population in Year 2050.", "Future-proofing major dam reservoirs and long-distance inter-basin water transfer projects."),
    ]

    for col, unit, is_key, sem_def, ai_guide in city_updates:
        conn.execute("""
        UPDATE _layer_attribute_dictionary
        SET unit_of_measurement = ?, is_thematic_key = ?, semantic_definition = ?, ai_interpretation_guide = ?
        WHERE table_name = ? AND column_name = ?
        """, (unit, is_key, sem_def, ai_guide, city_tbl, col))

    conn.commit()
    conn.close()
    print("Administrative population attribute dictionary enriched!")

if __name__ == "__main__":
    main()
