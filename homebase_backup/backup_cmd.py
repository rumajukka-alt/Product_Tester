# ----------------------------------------------
# Project ProductionTester
# V0.0
# Home base backup function
# homebase_backup/backup_cmd.py
# 18.01.2026
# ----------------------------------------------

"""
Command-line entry point for Homebase backup.
Currently only prints placeholder messages.
"""

from .sync_service import SyncService


def main():
    print("=== Homebase Backup Command ===")
    service = SyncService()
    service.run_backup()


if __name__ == "__main__":
    main()
