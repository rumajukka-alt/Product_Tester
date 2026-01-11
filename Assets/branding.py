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

        # Prefer the authoritative VERSION file at project root. If it differs
        # from branding.json, update branding.json on disk so files stay in sync.
        version_file = os.path.normpath(os.path.join(base_path, "..", "VERSION"))
        version_from_file = None
        try:
            with open(version_file, "r", encoding="utf-8") as vf:
                version_from_file = vf.read().strip()
        except Exception:
            version_from_file = None

        file_version = data.get("version", "")
        if version_from_file and version_from_file != file_version:
            # update branding.json on disk to keep source files consistent
            data["version"] = version_from_file
            try:
                with open(json_path, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
            except Exception:
                # If writing fails, fall back to using version_from_file in memory
                pass

        self.tool_name = data.get("tool_name", "Unnamed Tool")
        self.company_name = data.get("company_name", "")
        # use authoritative value (either from VERSION or branding.json)
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
