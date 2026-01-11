import os
import sys

# Add project root to PYTHONPATH
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from Code.test_runner import TestRunner  # noqa: E402
from Code.ui_logic import UILogic  # noqa: E402


class Ui_Keywords:
    def __init__(self):
        # Käytetään samaa runneria kuin test_api.py
        self.runner = TestRunner(start_ui=False)
        self.ui = UILogic(self.runner, headless=True)

    def press_start(self, spec_path: str):
        return self.ui.start_pressed(spec_path)

    def press_stop(self):
        return self.ui.stop_pressed()

    def press_cancel(self):
        return self.ui.cancel_pressed()


# Module-level instance and wrapper functions so Robot Framework
# sees keywords when importing the .py file as a library.
_ui = Ui_Keywords()


def press_start(spec_path: str):
    return _ui.press_start(spec_path)


def press_stop():
    return _ui.press_stop()


def press_cancel():
    return _ui.press_cancel()


def get_ui_status():
    # Return the UI status string
    return _ui.ui.status
