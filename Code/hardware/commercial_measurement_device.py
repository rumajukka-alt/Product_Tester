# ----------------------------------------------
# Project ProductionTester
# V0.1
# hardware/commercial_measurement_device.py
# Copyright BigJ
# 10.08.2026
# ----------------------------------------------

from Code.interfaces.measurement_device_interface import MeasurementDeviceInterface

class CommercialMeasurementDevice(MeasurementDeviceInterface):

    def __init__(self, accuracy_percent):
        self.accuracy = accuracy_percent
        # TODO: initialize real hardware connection

    def read_current_mA(self) -> float:
        # TODO: read from real hardware
        raise NotImplementedError("Real hardware not yet implemented")

    def get_accuracy_percent(self) -> float:
        return self.accuracy