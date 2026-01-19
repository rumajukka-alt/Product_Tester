#!/usr/bin/env python3
"""
Generate realistic limits by running fast simulation samples.

Writes updated Spec/limits.json (backs up original to limits.json.bak).
"""

import argparse
import json
import math
import os
import random
import shutil

from Code.simulator.config import SimulatorConfig


def simulate_sample(
    nominal=25.0,
    temp_coeff=0.15,
    tolerance=5.0,
    accuracy_percent=1.0,
    shunt_nominal=100.0,
    shunt_temp_coeff_ppm=150.0,
    wiring_noise_mA=0.5,
):
    """Return one simulated measured current (mA) without sleeping."""

    # Device-specific offset (device-to-device variation)
    device_offset = random.uniform(-tolerance, tolerance) / 100.0

    # Temperature sampled from environment config
    min_t = SimulatorConfig.environment.MIN_TEMPERATURE_C
    max_t = SimulatorConfig.environment.MAX_TEMPERATURE_C
    temp = random.uniform(min_t, max_t)
    delta_temp = temp - 25.0

    # Base current with device offset
    base = nominal * (1.0 + device_offset)

    # Temperature effect on product current
    temp_factor = 1.0 + (delta_temp * (temp_coeff / 100.0))
    product_current = base * temp_factor

    # Product noise (mV -> mA sensitivity as in ProductSample)
    noise_mV = random.uniform(
        -SimulatorConfig.environment.ENV_NOISE_mV,
        SimulatorConfig.environment.ENV_NOISE_mV,
    )
    noise_effect_mA = (noise_mV / 1000.0) * 0.02

    # Device read: includes accuracy error and its own noise contribution
    accuracy_error = product_current * (accuracy_percent / 100.0)
    accuracy_offset = random.uniform(-accuracy_error, accuracy_error)

    device_reading = product_current + noise_effect_mA + accuracy_offset

    # Shunt resistor drift effect (scaling error)
    drift_factor = 1.0 + (shunt_temp_coeff_ppm * delta_temp) / 1_000_000.0
    shunt_value = shunt_nominal * drift_factor
    scaling_error = (shunt_value - shunt_nominal) / shunt_nominal
    shunt_effect = product_current * scaling_error

    # Wiring noise
    wiring_effect = random.uniform(-wiring_noise_mA, wiring_noise_mA)

    # Environmental noise contribution to measurement circuit (mV -> mA)
    env_noise_mA = noise_mV / 1000.0

    measured = device_reading + shunt_effect + wiring_effect + env_noise_mA
    return measured


def generate(samples=10000, out_path="Spec/limits.json", backup=True):
    vals = []
    for _ in range(samples):
        vals.append(simulate_sample())

    mean = sum(vals) / len(vals)
    # population std (use sample std? for limits, population std is fine)
    var = sum((x - mean) ** 2 for x in vals) / len(vals)
    sigma = math.sqrt(var)

    min_limit = mean - 3 * sigma
    max_limit = mean + 3 * sigma

    # Read existing file and backup
    base_dir = os.path.dirname(os.path.dirname(__file__))
    spec_path = os.path.join(base_dir, out_path)
    if backup and os.path.exists(spec_path):
        shutil.copy2(spec_path, spec_path + ".bak")

    new_spec = {
        "current": {
            "min": round(min_limit, 6),
            "typ": round(mean, 6),
            "max": round(max_limit, 6),
        }
    }

    with open(spec_path, "w", encoding="utf-8") as f:
        json.dump(new_spec, f, indent=4)

    return {
        "samples": samples,
        "mean": mean,
        "sigma": sigma,
        "min": min_limit,
        "max": max_limit,
        "path": spec_path,
    }


def main():
    parser = argparse.ArgumentParser(description="Generate limits from fast simulation")
    parser.add_argument("-n", "--samples", type=int, default=10000, help="Number of samples")
    parser.add_argument(
        "--no-backup",
        dest="backup",
        action="store_false",
        help="Do not backup existing limits.json",
    )
    args = parser.parse_args()

    out = generate(samples=args.samples, backup=args.backup)

    print(f"Samples: {out['samples']}")
    print(f"Mean (typ): {out['mean']:.6f} mA")
    print(f"Sigma: {out['sigma']:.6f} mA")
    print(f"Min (mean-3*sigma): {out['min']:.6f} mA")
    print(f"Max (mean+3*sigma): {out['max']:.6f} mA")
    print(f"Wrote: {out['path']}")


if __name__ == "__main__":
    main()
