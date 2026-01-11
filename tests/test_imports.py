import importlib
import os
import sys

# Ensure project root is on sys.path when running pytest from tests/
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)


def test_import_main():
    importlib.import_module("main")


def test_import_core_modules():
    modules = [
        "Code.spec_loader",
        "Code.test_runner",
        "Code.simulator.simulator",
        "Code.simulator.simulated_measurement_device",
    ]
    for m in modules:
        importlib.import_module(m)
