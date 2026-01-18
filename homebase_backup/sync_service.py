# ----------------------------------------------
# Project ProductionTester
# V0.0
# Home base backup function
# homebase_backup/sync_service.py
# 18.01.2026
# ----------------------------------------------

"""
SyncService is responsible for orchestrating the backup process.
Actual upload logic will be added later.
"""

from .connection_check import has_connection
from .file_finder import find_files_to_sync


class SyncService:
    def __init__(self):
        pass

    def run_backup(self):
        print("Checking network connection...")

        if not has_connection():
            print("No connection available. Backup skipped.")
            return

        print("Connection OK.")
        files = find_files_to_sync()

        if not files:
            print("No files to sync.")
            return

        print("Files ready for backup:")
        for f in files:
            print(f" - {f}")

        print("Backup placeholder: no upload implemented yet.")
