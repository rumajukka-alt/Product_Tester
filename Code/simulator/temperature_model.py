# ----------------------------------------------
# Project ProductionTester
# V0.1
# simulator/temperature_model.py
# Copyright BigJ
# 10.08.2026
# ----------------------------------------------

import random
from Code.simulator.config import SimulatorConfig

class TemperatureModel:
    """
    Provides a simulated production environment temperature (°C).
    """

    def __init__(self):
        self.min_temp = SimulatorConfig.environment.MIN_TEMPERATURE_C
        self.max_temp = SimulatorConfig.environment.MAX_TEMPERATURE_C

    def get_temperature_C(self) -> float:
        """
        Returns a random temperature within the configured production range.
        """
        return random.uniform(self.min_temp, self.max_temp)