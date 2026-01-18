# ----------------------------------------------
# Project ProductionTester
# V0.0
# Home base backup function
# homebase_backup/connection_check.py
# 18.01.2026
# ----------------------------------------------

"""
Simple network connectivity check.
Later this can be extended to check Homebase server availability.
"""

import socket


def has_connection(host="8.8.8.8", port=53, timeout=2):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except OSError:
        return False
