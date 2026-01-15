# ----------------------------------------------
# Prototype_run.py
# NOT FOR PRODUCTION JUST FOR TESTING
# V0.1
# 14.1.2026
# Batch test runner for ProductionTester
# ----------------------------------------------

import sys

from Code.test_runner import TestRunner


def main():
    # Argument check
    if len(sys.argv) < 2:
        print("Usage: py Prototype_run.py <count>")
        return

    try:
        count = int(sys.argv[1])
    except ValueError:
        print("Count must be an integer")
        return

    print(f"Starting batch run of {count} tests...")

    # Create TestRunner without UI
    runner = TestRunner(start_ui=False)

    for i in range(count):
        measured, result = runner.run_test()
        print(f"{i+1}/{count}: {measured:.3f} mA → {result}")

    print("Batch run complete.")


if __name__ == "__main__":
    main()
