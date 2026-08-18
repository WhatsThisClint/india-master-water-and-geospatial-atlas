"""
publish_new_version.py
Automates bumping version, committing changes, tagging, and creating a GitHub Release.

Usage:
    python scripts/publish_new_version.py <version_tag> <release_title> [notes_file]

Example:
    python scripts/publish_new_version.py v1.1.0 "Added new microwatersheds and 2024 rainfall data"
"""

import sys
import os
import subprocess

def run_cmd(cmd):
    print(f">> Running: {cmd}")
    res = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    if res.returncode != 0:
        print(f"Error ({res.returncode}): {res.stderr}")
        sys.exit(res.returncode)
    print(res.stdout)
    return res.stdout

def main():
    if len(sys.argv) < 3:
        print("Usage: python scripts/publish_new_version.py <version_tag> <release_title> [notes_file]")
        print("Example: python scripts/publish_new_version.py v1.1.0 'Updated Aquifers' notes.md")
        sys.exit(1)

    tag = sys.argv[1]
    title = sys.argv[2]
    notes_file = sys.argv[3] if len(sys.argv) > 3 else None

    print(f"=== PUBLISHING NEW RELEASE: {tag} ({title}) ===")

    # 1. Git add & commit
    run_cmd("git add .")
    try:
        run_cmd(f'git commit -m "release: {tag} - {title}"')
    except Exception:
        print("No new changes to commit, proceeding with tag/release...")

    # 2. Push commits
    run_cmd("git push origin main")

    # 3. Create GitHub Release via gh CLI
    if notes_file and os.path.exists(notes_file):
        cmd = f'gh release create {tag} -F "{notes_file}" --title "{title}"'
    else:
        cmd = f'gh release create {tag} --generate-notes --title "{title}"'

    run_cmd(cmd)
    print(f"\n🎉 Successfully published release {tag} on GitHub!")

if __name__ == "__main__":
    main()
