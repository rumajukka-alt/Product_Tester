# ----------------------------------------------
# Project ProductionTester
# V0.4
# Button logic added
# Code/test_runner.py
# ----------------------------------------------

from typing import Optional, Tuple

from Code.simulator.measurement_circuit import MeasurementCircuit
from Code.simulator.product_sample import ProductSample
from Code.simulator.simulated_measurement_device import SimulatedMeasurementDevice
from Code.spec_loader import load_limits
from data_logging.device_logger import DeviceLogger
from data_logging.result_writer import ResultWriter


class TestRunner:
    def __init__(self, start_ui: bool = True):
        self.start_ui = start_ui

        # Logging modules
        self.logger = DeviceLogger(base_path="data_logging/device_log")
        self.results = ResultWriter(
            base_path="data_logging/results_LOG", tester_id="Tester01"
        )

        # Core logic
        self.product = ProductSample()
        self.device = SimulatedMeasurementDevice(self.product, accuracy_percent=1.0)
        self.circuit = MeasurementCircuit(self.device)
        self.limits = load_limits()["current"]

        # Optional UI
        self.ui = None
        if self.start_ui:
            from UI.main_window import MainWindow

            self.ui = MainWindow()

        # Control flags
        self.cancel_requested = False
        self.stop_requested = False

    def request_cancel(self) -> None:
        self.cancel_requested = True

    def request_stop(self) -> None:
        self.stop_requested = True

    def run_test(self, spec_path: Optional[str] = None) -> Tuple[float, str]:

        # --- LOG: test start ---
        self.logger.write("Test started")

        # Perform measurement
        measured = self.circuit.measure_current_mA()

        # Read temperature
        temp_C = self.device.read_temperature_C()

        # --- LOG: measured values ---
        self.logger.write(f"Measured current = {measured} mA")
        self.logger.write(f"Measured temperature = {temp_C} C")

        # Limits
        min_limit = self.limits["min"]
        max_limit = self.limits["max"]

        # PASS/FAIL
        result = "PASS" if min_limit <= measured <= max_limit else "FAIL"

        # --- LOG: result ---
        self.logger.write(f"Result = {result}")

        # Save result
        ppid = "PPIDTEST001"

        self.results.write_result(
            ppid=ppid,
            result=result,
            data_dict={"current_mA": measured, "temperature_C": temp_C},
        )

        # Reset flags
        self.cancel_requested = False
        self.stop_requested = False

        return measured, result

    def run(self, spec_path: Optional[str] = None) -> Tuple[float, str]:
        return self.run_test(spec_path)
