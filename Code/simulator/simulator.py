# ----------------------------------------------
# Project ProductionTester
# V0.1
# simulator/simulator.py
# Copyright BigJ
# 10.08.2026
# ----------------------------------------------

from Code.simulator.measurement_circuit import MeasurementCircuit
from Code.simulator.product_sample import ProductSample


class ProductionTesterSimulator:

    def __init__(self):
        self.product = ProductSample(nominal_current_mA=25.0)
        self.measurement = MeasurementCircuit(self.product)

    def run_measurement(self):
        return self.measurement.measure_current_mA()
