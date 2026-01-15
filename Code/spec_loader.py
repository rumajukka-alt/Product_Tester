# ----------------------------------------------
# Project ProductionTester
# V0.1
# Code/spec_loader.py
# Copyright BigJ
# 11.01.2026
# ----------------------------------------------

import json
import os


def load_limits():
    base_dir = os.path.dirname(os.path.dirname(__file__))  # Production_Tester/
    spec_path = os.path.join(base_dir, "Spec", "limits.json")

    with open(spec_path, "r") as f:
        return json.load(f)
