# ----------------------------------------------
# Project ProductionTester
# V0.1
# UI/pass_fail_indicator.py
# Copyright BigJ
# 11.02.2026
# ----------------------------------------------

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QSizePolicy


class PassFailIndicator(QLabel):
    def __init__(self):
        super().__init__("IDLE")

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setFixedHeight(120)
        self.setFixedWidth(600)

        # Tämä tekee siitä yhtä leveän kuin oskilloskooppi
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        self.setStyleSheet("""
            QLabel {
                background-color: #cccc00;   /* keltainen IDLE */
                color: black;
                font-size: 32px;
                border-radius: 12px;
                border: 2px solid #666;
            }
        """)

    def set_state(self, state):
        if state == "running":
            self.setText("RUNNING")
            self.setStyleSheet("background-color: yellow; font-size: 32px;")
        elif state == "pass":
            self.setText("PASS")
            self.setStyleSheet(
                "background-color: green; color: white; font-size: 32px;"
            )
        elif state == "fail":
            self.setText("FAIL")
            self.setStyleSheet("background-color: red; color: white; font-size: 32px;")
        else:
            self.setText("IDLE")
            self.setStyleSheet("background-color: #cccc00; font-size: 32px;")
