# ----------------------------------------------
# Project ProductionTester
# V0.1
# interfaces/measurement_device_interface.py
# Copyright BigJ
# 10.08.2026
# ----------------------------------------------


from abc import ABC, abstractmethod


class MeasurementDeviceInterface(ABC):
    """
    Abstract interface for any current measurement device (commercial or simulated).
    """

    @abstractmethod
    def read_current_mA(self) -> float:
        """Return measured current in milliamps."""
        pass

    @abstractmethod
    def get_accuracy_percent(self) -> float:
        """Return the device's specified accuracy in percent."""
        pass
