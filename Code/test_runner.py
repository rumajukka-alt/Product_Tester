# ----------------------------------------------
# Project ProductionTester
# V0.2
# Button logic added
# Code/test_runner.py
# Copyright BigJ
# 10.08.2026
# ----------------------------------------------


from Code.simulator.measurement_circuit import MeasurementCircuit
from Code.simulator.product_sample import ProductSample
from Code.simulator.simulated_measurement_device import SimulatedMeasurementDevice
from Code.spec_loader import load_limits


class TestRunner:
    def __init__(self):
        self.product = ProductSample()
        self.device = SimulatedMeasurementDevice(self.product, accuracy_percent=1.0)
        self.circuit = MeasurementCircuit(self.device)
        self.limits = load_limits()["current"]

        # Keskeytysliput, joita UI ohjaa
        self.cancel_requested = False
        self.stop_requested = False

    # UI kutsuu, kun CANCEL painetaan
    def request_cancel(self):
        self.cancel_requested = True

    # UI kutsuu, kun STOP painetaan
    def request_stop(self):
        self.stop_requested = True

    def run_test(self):
        """
        Suorittaa mittauksen. Tämä ajetaan taustasäikeessä TestWorkerin kautta.
        Keskeytys tarkistetaan TestWorkerissä ennen ja jälkeen kutsun.
        """

        measured = self.circuit.measure_current_mA()

        min_limit = self.limits["min"]
        max_limit = self.limits["max"]

        result = "PASS" if min_limit <= measured <= max_limit else "FAIL"

        # Nollaa liput testin jälkeen; jos keskeytys on tullut,
        # TestWorker tulkitsee sen aborted-tilaksi eikä käytä tätä tulosta.
        self.cancel_requested = False
        self.stop_requested = False

        return measured, result
