# ----------------------------------------------
# Project ProductionTester
# V0.0
# Home base backup function
# homebase_backup/file_finder.py
# 18.01.2026
# ----------------------------------------------

"""
Finds result CSV files and log files that should be backed up.
Later we can add metadata tracking to avoid duplicate uploads.
"""

import glob


def find_files_to_sync():
    files = []

    # Adjust these paths to match your project structure
    files.extend(glob.glob("data_logging/*.csv"))
    files.extend(glob.glob("logs/*.txt"))

    return files
