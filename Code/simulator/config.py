# ----------------------------------------------
# Project ProductionTester
# V0.1
# simulator/config.py
# Copyright BigJ
# 11.01.2026
# ----------------------------------------------

"""
Simulation configuration for production tester environment.
Defines temperature variation and measurement circuit noise.
"""


class EnvironmentConfig:
    # Production temperature range (°C)
    MIN_TEMPERATURE_C = 22.0
    MAX_TEMPERATURE_C = 35.0

    # Environmental electrical noise in measurement circuit (mV)
    ENV_NOISE_mV = 200.0


class SimulatorConfig:
    """
    High-level container for all simulator-related configuration.
    More parameters (e.g., drift, offsets, ADC resolution) can be added later.
    """

    environment = EnvironmentConfig
