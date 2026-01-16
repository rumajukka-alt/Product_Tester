import os
import sys
from pathlib import Path

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from Code.test_runner import TestRunner  # noqa: E402

# Varmista että hakemisto ja tiedosto ovat olemassa
Path("data_logging/results_LOG").mkdir(parents=True, exist_ok=True)
if not os.path.exists("data_logging/results_LOG/results_2026-01.csv"):
    # Luo tyhjä CSV-tiedosto oletusotsikoilla
    with open("data_logging/results_LOG/results_2026-01.csv", "w") as f:
        f.write("date,time,result\n")  # Muuta otsikot tarpeen mukaan


class Test_Api:
    def __init__(self):
        self.runner = TestRunner(start_ui=False)

    def run_test(self, spec_path: str):
        return self.runner.run_test(spec_path)

    def get_last_result(self):
        return getattr(self.runner, "last_result", None)


# Module-level instance and wrapper functions so Robot Framework
# sees keywords when importing the .py file as a library.
_api = Test_Api()


def run_test(spec_path: str):
    return _api.run_test(spec_path)


def get_last_result():
    return _api.get_last_result()
