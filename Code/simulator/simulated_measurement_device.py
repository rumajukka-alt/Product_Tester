# ----------------------------------------------
# Project ProductionTester
# V0.1
# simulator/simulated_measurement_device.py
# Copyright BigJ
# 10.08.2026
# ----------------------------------------------

import random

from Code.interfaces.measurement_device_interface import MeasurementDeviceInterface
from Code.simulator.noise_model import NoiseModel
from Code.simulator.temperature_model import TemperatureModel


class SimulatedMeasurementDevice(MeasurementDeviceInterface):

    def __init__(self, product, accuracy_percent=1.0):
        self.product = product
        self.temperature = TemperatureModel()
        self.noise = NoiseModel()
        self.accuracy = accuracy_percent

    def read_current_mA(self) -> float:
        # Base current from product
        base_current = self.product.get_expected_current_mA()

        # Environmental noise (mV → mA conversion left simple for now)
        noise_mA = self.noise.get_noise_mV() / 1000.0

        # Device accuracy error
        accuracy_error = base_current * (self.accuracy / 100.0)
        accuracy_offset = random.uniform(-accuracy_error, accuracy_error)

        return base_current + noise_mA + accuracy_offset

    def get_accuracy_percent(self) -> float:
        return self.accuracy

    def read_temperature_C(self) -> float:
        """
        Palauttaa viimeisimmän lämpötilan, jota käytettiin virran laskennassa.
        """
        return self.product.get_last_temperature_C()
