# ----------------------------------------------
# Project ProductionTester
# V0.1
# Button logic added
# Code/test_worker.py
# Copyright BigJ
# 10.08.2026
# ----------------------------------------------


from PyQt6.QtCore import QObject, pyqtSignal


class TestWorker(QObject):
    finished = pyqtSignal(float, str)  # value, result
    aborted = pyqtSignal()             # keskeytetty (CANCEL/STOP)

    def __init__(self, test_runner):
        super().__init__()
        self.test_runner = test_runner

    def run(self):
        # Keskeytys ennen testin alkua
        if self.test_runner.cancel_requested or self.test_runner.stop_requested:
            self.aborted.emit()
            return

        value, result = self.test_runner.run_test()

        # Jos CANCEL/STOP painettu mittauksen aikana,
        # tulkitaan koko testi keskeytetyksi, ei luotettavaksi tulokseksi.
        if self.test_runner.cancel_requested or self.test_runner.stop_requested:
            self.aborted.emit()
            return

        self.finished.emit(value, result)