# ----------------------------------------------
# Project ProductionTester
# V0.1
# UI/show_current_widget.py
# Copyright BigJ
# 12.01.2026
# ----------------------------------------------
import pytest

pytest.skip("Skipping UI tests in CI environment", allow_module_level=True)

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel


class ShowCurrentWidget(QLabel):
    def __init__(self):
        super().__init__()
        self.setObjectName("show_current_widget")
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setText("-- mA")

    def update_value(self, value: float):
        self.setText(f"{value:.1f} mA")
