"""
fast_deep_audit_tables.py
Fast deep audit of all tables and columns without heavy full table scans.
"""

import sqlite3

GPKG_PATH = r"F:\Antigravity\Hydrosheds and Basins\hydrosheds_consolidated_master.gpkg"

def main():
    conn = sqlite3.connect(GPKG_PATH)
    tables = [t[0] for t in conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()]

    report = []
    for tbl in sorted(tables):
        if tbl.startswith(('gpkg_', 'rtree_', 'sqlite_')):
            continue
        cols = conn.execute(f'PRAGMA table_info("{tbl}")').fetchall()
        count = conn.execute(f'SELECT count(*) FROM "{tbl}"').fetchone()[0]
        
        report.append(f"================================================================================")
        report.append(f"TABLE: {tbl} (Total Rows: {count:,})")
        report.append(f"================================================================================")
        
        for c in cols:
            cid, cname, ctype, notnull, dflt, pk = c
            if cname in ['geom', 'fid', 'id']:
                continue
            
            try:
                samples = conn.execute(f'SELECT DISTINCT "{cname}" FROM "{tbl}" WHERE "{cname}" IS NOT NULL AND "{cname}" != "" LIMIT 4').fetchall()
                sample_str = ", ".join([str(s[0])[:35] for s in samples])
                report.append(f"  - {cname} ({ctype}) -> Samples: [{sample_str}]")
            except Exception as e:
                report.append(f"  - {cname} ({ctype}) -> Error: {e}")
        report.append("\n")

    conn.close()

    with open("F:/Antigravity/Hydrosheds and Basins/full_table_attribute_deep_audit.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(report))
    print(f"Deep audit written to full_table_attribute_deep_audit.txt ({len(report)} lines)")

if __name__ == "__main__":
    main()
