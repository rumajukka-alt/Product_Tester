# ----------------------------------------------
# Project ProductionTester
# V0.1
# simulator/simulator.py
# Copyright BigJ
# 10.08.2026
# ----------------------------------------------

from Code.simulator.measurement_circuit import MeasurementCircuit
from Code.simulator.product_sample import ProductSample
from Code.simulator.simulated_measurement_device import SimulatedMeasurementDevice


class ProductionTesterSimulator:

    def __init__(self):
        self.product = ProductSample(nominal_current_mA=25.0)
        # Create a simulated measurement device that references the product
        self.device = SimulatedMeasurementDevice(self.product, accuracy_percent=1.0)
        # MeasurementCircuit expects a measurement device.
        # The device provides `.product` and `read_current_mA()` used by the
        # measurement pipeline.
        self.measurement = MeasurementCircuit(self.device)

    def run_measurement(self):
        return self.measurement.measure_current_mA()
