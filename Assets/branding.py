# ----------------------------------------------
# Project ProductionTester
# V0.1
# Button logic added
# Assets/branding.py
# Copyright BigJ
# 10.08.2026
# ----------------------------------------------


import json
import os


class Branding:
    def __init__(self):
        base_path = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(base_path, "branding.json")

        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.tool_name = data.get("tool_name", "Unnamed Tool")
        self.company_name = data.get("company_name", "")
        self.version = data.get("version", "")
        self.ui_brand_color = data.get("ui_brand_color", "#444a80")
        self.copyright = data.get(
            "copyright", f"© {self.company_name}" if self.company_name else ""
        )

    def window_title(self):
        """Palauttaa valmiin otsikon MainWindowille."""
        if self.version:
            return f"{self.tool_name}  —  v{self.version}"
        return self.tool_name
