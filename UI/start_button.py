# ----------------------------------------------
# Project ProductionTester
# V0.2
# UI/start_button.py
# Copyright BigJ
# 10.08.2026
# ----------------------------------------------

from PyQt6.QtWidgets import QPushButton


class StartButton(QPushButton):
    def __init__(self):
        super().__init__("START")
        self.setFixedHeight(80)
        self.set_ready()

    def set_ready(self):
        self.setText("START")
        self.setEnabled(True)
        self.setStyleSheet(
            """
            QPushButton {
                background-color: #2ecc71;
                color: white;
                font-size: 28px;
                border-radius: 12px;
            }
        """
        )

    def set_running(self):
        self.setText("RUNNING")
        self.setEnabled(False)
        self.setStyleSheet(
            """
            QPushButton {
                background-color: #e74c3c;
                color: white;
                font-size: 28px;
                border-radius: 12px;
            }
        """
        )
