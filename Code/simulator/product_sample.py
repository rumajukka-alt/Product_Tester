# ----------------------------------------------
# Project ProductionTester
# V0.3
# Test delay added
# simulator/product_sample.py
# Copyright BigJ
# 10.08.2026
# ----------------------------------------------

import random
import time

from Code.simulator.noise_model import NoiseModel
from Code.simulator.temperature_model import TemperatureModel


class ProductSample:
    """
    Simulated production device (e.g., LDO regulator module)
    whose current consumption depends on temperature and noise.
    """

    def __init__(
        self,
        nominal_current_mA: float = 25.0,
        temp_coeff_percent_per_C: float = 0.15,
        internal_tolerance_percent: float = 5.0,
    ):
        """
        nominal_current_mA: base current at 25°C
        temp_coeff_percent_per_C: how much current changes per °C
        internal_tolerance_percent: device-to-device variation
        """
        self.nominal = nominal_current_mA
        self.temp_coeff = temp_coeff_percent_per_C
        self.tolerance = internal_tolerance_percent

        self.temperature = TemperatureModel()
        self.noise = NoiseModel()

        # Each device has its own internal offset
        self.device_offset = random.uniform(-self.tolerance, self.tolerance) / 100.0

    def get_expected_current_mA(self) -> float:
        """
        Returns the device's current consumption including:
        - temperature effect
        - internal tolerance
        - noise sensitivity
        """

        # Simuloi todellinen mittausaika (1–10 sekuntia)
        time.sleep(random.uniform(1.0, 10.0))

        # Base current with device-specific offset
        base = self.nominal * (1.0 + self.device_offset)

        # Temperature effect
        temp = self.temperature.get_temperature_C()
        delta_temp = temp - 25.0  # reference temperature
        temp_factor = 1.0 + (delta_temp * (self.temp_coeff / 100.0))

        # Noise effect (convert mV → mA sensitivity)
        noise_mV = self.noise.get_noise_mV()
        noise_effect_mA = noise_mV * 0.02  # 2% of noise magnitude affects current

        return base * temp_factor + noise_effect_mA
