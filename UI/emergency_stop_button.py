import pytest

pytest.skip("Skipping UI tests in CI environment", allow_module_level=True)

# ----------------------------------------------
# Project ProductionTester
# V0.2
# UI/emergency_stop_button.py
# Copyright BigJ
# 11.01.2026
# ----------------------------------------------


from PyQt6.QtWidgets import QPushButton


class EmergencyStopButton(QPushButton):
    def __init__(self):
        super().__init__("STOP")
        self.setFixedSize(120, 120)
        self.setStyleSheet("""
            QPushButton {
                background-color: red;
                color: white;
                font-size: 28px;
                border-radius: 60px;   /* half of width/height → round */
                border: 4px solid darkred;
            }
            QPushButton:pressed {
                background-color: #aa0000;
            }
        """)
