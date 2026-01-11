import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from Code.simulator.simulator import ProductionTesterSimulator  # noqa: E402


class MeasurementKeywords:
    def __init__(self):
        self.device = ProductionTesterSimulator()

    def measure_current(self):
        return self.device.run_measurement()


# Module-level instance and wrapper functions so Robot Framework
# sees keywords when importing the .py file as a library.
_measurement = MeasurementKeywords()


def measure_current():
    return _measurement.measure_current()
