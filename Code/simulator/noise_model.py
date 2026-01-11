# ----------------------------------------------
# Project ProductionTester
# V0.1
# simulator/noise_model.py
# Copyright BigJ
# 10.08.2026
# ----------------------------------------------

import random
from Code.simulator.config import SimulatorConfig

class NoiseModel:
    """
    Provides environmental electrical noise (in mV) for the measurement circuit.
    """

    def __init__(self):
        self.noise_mV = SimulatorConfig.environment.ENV_NOISE_mV

    def get_noise_mV(self) -> float:
        """
        Returns a random noise value between -noise_mV and +noise_mV.
        """
        return random.uniform(-self.noise_mV, self.noise_mV)