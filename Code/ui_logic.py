# Code/ui_logic.py


class UILogic:
    def __init__(self, runner, headless: bool = False):
        self.runner = runner
        self.headless = headless

        # UI state
        self.status = "Idle"
        self.progress = 0

    # -------------------------
    # UI actions (logic only)
    # -------------------------

    def start_pressed(self, spec_path: str):
        """UI Start button logic."""
        self.status = "Running"
        result = self.runner.run(spec_path)
        self.status = "Finished"
        return result

    def stop_pressed(self):
        """UI Stop button logic."""
        self.runner.request_stop()
        self.status = "Stopped"

    def cancel_pressed(self):
        """UI Cancel button logic."""
        self.runner.request_cancel()
        self.status = "Cancelled"

    # -------------------------
    # UI state updates
    # -------------------------

    def update_status(self, text: str):
        self.status = text

    def update_progress(self, value: int):
        self.progress = value
