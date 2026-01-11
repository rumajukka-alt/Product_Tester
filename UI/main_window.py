# ----------------------------------------------
# Project ProductionTester
# V0.5
# UI/main_window.py
# Copyright BigJ
# 10.08.2026
# ----------------------------------------------

from PyQt6.QtCore import QThread
from PyQt6.QtWidgets import QGridLayout, QMainWindow, QPushButton, QWidget

from Assets.branding import Branding
from Code.spec_loader import load_limits
from Code.test_runner import TestRunner
from Code.test_worker import TestWorker
from UI.emergency_stop_button import EmergencyStopButton
from UI.oscilloscope_widget import OscilloscopeWidget
from UI.pass_fail_indicator import PassFailIndicator
from UI.start_button import StartButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # --- Branding ---
        self.brand = Branding()
        self.setWindowTitle(self.brand.window_title())

        # --- Test Runner ---
        self.test_runner = TestRunner()

        # --- UI Widgets ---
        self.osc = OscilloscopeWidget()
        self.result_indicator = PassFailIndicator()
        self.start_button = StartButton()

        # CANCEL
        self.cancel_button = QPushButton("CANCEL")
        self.cancel_button.setObjectName("cancel_button")  # 🔥 QSS tunnistaa tämän
        self.cancel_button.setFixedHeight(80)
        self.cancel_button.setFixedWidth(400)
        self.cancel_button.clicked.connect(self.cancel_test)

        # STOP
        self.stop_button = EmergencyStopButton()
        self.stop_button.clicked.connect(self.stop_test)

        # Footer
        self.footer = QPushButton(self.brand.copyright)
        self.footer.setEnabled(False)
        self.footer.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                color: gray;
                font-size: 12px;
                border: none;
            }
        """
        )

        # --- Load limits from JSON ---
        limits = load_limits()
        self.osc.set_limits(limits["current"]["min"], limits["current"]["max"])

        # --- Thread-related members ---
        self.thread = None
        self.worker = None

        # --- Connect START button ---
        self.start_button.clicked.connect(self.start_test)

        # --- Layout ---
        central = QWidget()
        layout = QGridLayout(central)

        # 🔥 Layout-marginaalit (QSS ei tue layout-selektoreita)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setHorizontalSpacing(20)
        layout.setVerticalSpacing(20)

        layout.addWidget(self.osc, 0, 0)
        layout.addWidget(self.result_indicator, 1, 0)
        layout.addWidget(self.start_button, 0, 1)
        layout.addWidget(self.cancel_button, 1, 1)
        layout.addWidget(self.stop_button, 2, 1)
        layout.addWidget(self.footer, 3, 0, 1, 2)

        self.setCentralWidget(central)

    # ----------------------------------------------------
    # START painettu → nappi RUNNING ja testi säikeeseen
    # ----------------------------------------------------
    def start_test(self):
        print("DEBUG: start_test CALLED")

        if self.thread is not None and self.thread.isRunning():
            print("DEBUG: Test already running, ignoring START")
            return

        # 🔥 START-nappi RUNNING-tilaan (QSS override)
        self.start_button.set_running()

        # Reset flags
        self.test_runner.cancel_requested = False
        self.test_runner.stop_requested = False

        # Thread + worker
        self.thread = QThread()
        self.worker = TestWorker(self.test_runner)
        self.worker.moveToThread(self.thread)

        # Signals
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.on_test_finished)
        self.worker.aborted.connect(self.on_test_aborted)

        # Cleanup
        self.worker.finished.connect(self.thread.quit)
        self.worker.aborted.connect(self.thread.quit)
        self.thread.finished.connect(self.on_thread_finished)

        self.thread.start()

    # ----------------------------------------------------
    # Testi valmis normaalisti
    # ----------------------------------------------------
    def on_test_finished(self, value, result):
        print("DEBUG: test finished")

        self.osc.set_value(value)

        # 🔥 PASS/FAIL QSS property
        self.result_indicator.set_state(result.lower())

        # 🔥 START-nappi READY-tilaan
        self.start_button.set_ready()

    # ----------------------------------------------------
    # Testi keskeytetty
    # ----------------------------------------------------
    def on_test_aborted(self):
        print("DEBUG: test aborted")

        self.result_indicator.set_state("fail")
        self.start_button.set_ready()

    # ----------------------------------------------------
    # Säie lopetti
    # ----------------------------------------------------
    def on_thread_finished(self):
        print("DEBUG: thread finished")
        self.thread = None
        self.worker = None

    # ----------------------------------------------------
    # CANCEL
    # ----------------------------------------------------
    def cancel_test(self):
        print("DEBUG: CANCEL pressed")
        self.test_runner.request_cancel()

    # ----------------------------------------------------
    # STOP
    # ----------------------------------------------------
    def stop_test(self):
        print("DEBUG: STOP pressed")
        self.test_runner.request_stop()

        self.result_indicator.set_state("fail")
        self.start_button.set_ready()
