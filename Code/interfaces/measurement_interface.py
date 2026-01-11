# ----------------------------------------------
# Project ProductionTester
# V0.1
# interfaces/measurement_interface.py
# Copyright BigJ
# 10.08.2026
# ----------------------------------------------

from abc import ABC, abstractmethod

class MeasurementInterface(ABC):

    @abstractmethod
    def measure_current_mA(self) -> float:
        """Return measured current in milliamps."""
        pass