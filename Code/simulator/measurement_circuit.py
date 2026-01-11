# ----------------------------------------------
# Project ProductionTester
# V0.2
# simulator/measurement_circuit.py
# Copyright BigJ
# 10.08.2026
# ----------------------------------------------


import random
from Code.interfaces.measurement_device_interface import MeasurementDeviceInterface
from Code.simulator.temperature_model import TemperatureModel
from Code.simulator.noise_model import NoiseModel

class MeasurementCircuit:
    """
    Simulates a real measurement circuit between the product and the measurement device.
    Includes:
    - shunt resistor drift with temperature
    - wiring/connector noise
    - environmental noise
    """

    def __init__(self,
                 measurement_device: MeasurementDeviceInterface,
                 shunt_resistor_milliohm: float = 100.0,
                 shunt_temp_coeff_ppm: float = 150.0,
                 wiring_noise_mA: float = 0.5):
        """
        shunt_resistor_milliohm: nominal shunt value
        shunt_temp_coeff_ppm: temperature drift (ppm/°C)
        wiring_noise_mA: random wiring/connector noise
        """
        self.device = measurement_device
        self.shunt_nominal = shunt_resistor_milliohm
        self.shunt_temp_coeff = shunt_temp_coeff_ppm
        self.wiring_noise = wiring_noise_mA

        self.temperature = TemperatureModel()
        self.environment_noise = NoiseModel()

    def _shunt_resistor_value(self) -> float:
        """
        Returns shunt resistor value including temperature drift.
        """
        temp = self.temperature.get_temperature_C()
        delta_temp = temp - 25.0

        drift_factor = 1.0 + (self.shunt_temp_coeff * delta_temp) / 1_000_000.0
        return self.shunt_nominal * drift_factor

    def measure_current_mA(self) -> float:
        """
        Full measurement pipeline:
        - product current
        - shunt drift
        - wiring noise
        - environmental noise
        - measurement device accuracy
        """
        # Step 1: product current
        product_current = self.device.product.get_expected_current_mA()

        # Step 2: shunt drift (affects measurement scaling)
        shunt_value = self._shunt_resistor_value()
        scaling_error = (shunt_value - self.shunt_nominal) / self.shunt_nominal
        shunt_effect = product_current * scaling_error

        # Step 3: wiring noise
        wiring_effect = random.uniform(-self.wiring_noise, self.wiring_noise)

        # Step 4: environmental noise (mV → mA)
        env_noise_mA = self.environment_noise.get_noise_mV() / 1000.0

        # Step 5: measurement device reading (includes accuracy error)
        device_reading = self.device.read_current_mA()

        # Combine everything
        return device_reading + shunt_effect + wiring_effect + env_noise_mA