# ----------------------------------------------
# Project ProductionTester
# V0.6
# UI/main_window.py
# Copyright BigJ
# 12.01.2026
# ----------------------------------------------
import pytest

pytest.skip("Skipping UI tests in CI environment", allow_module_level=True)

from PyQt6.QtCore import Qt, QThread
from PyQt6.QtWidgets import QGridLayout, QMainWindow, QPushButton, QWidget

from Assets.branding import Branding
from Code.spec_loader import load_limits
from Code.test_runner import TestRunner
from Code.test_worker import TestWorker
from Code.ui_logic import UILogic
from UI.emergency_stop_button import EmergencyStopButton
from UI.oscilloscope_widget import OscilloscopeWidget
from UI.pass_fail_indicator import PassFailIndicator
from UI.show_current_widget import ShowCurrentWidget
from UI.start_button import StartButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # --- Branding ---
        self.brand = Branding()
        self.setWindowTitle(self.brand.window_title())

        # --- Test Runner (UI disabled here) ---
        self.test_runner = TestRunner(start_ui=False)

        # --- UILogic ---
        self.logic = UILogic(self.test_runner)

        # --- UI Widgets ---
        self.osc = OscilloscopeWidget()
        self.result_indicator = PassFailIndicator()
        self.start_button = StartButton()
        self.current_display = ShowCurrentWidget()  # <<< NEW WIDGET

        # CANCEL
        self.cancel_button = QPushButton("CANCEL")
        self.cancel_button.setObjectName("cancel_button")
        self.cancel_button.setFixedHeight(80)
        self.cancel_button.setFixedWidth(400)
        self.cancel_button.clicked.connect(self._on_cancel)

        # STOP
        self.stop_button = EmergencyStopButton()
        self.stop_button.clicked.connect(self._on_stop)

        # Footer
        self.footer = QPushButton(self.brand.copyright)
        self.footer.setEnabled(False)
        self.footer.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: gray;
                font-size: 12px;
                border: none;
            }
        """)

        # --- Load limits from JSON ---
        limits = load_limits()
        # Synkataan UI:n ja TestRunnerin raja-arvot.
        # Molemmat käyttävät samaa lähdettä (limits.json).
        self.test_runner.limits = limits["current"]
        self.osc.set_limits(limits["current"]["min"], limits["current"]["max"])

        # --- Thread-related members ---
        self.thread = None
        self.worker = None

        # --- Connect START button ---
        self.start_button.clicked.connect(self._on_start)

        # --- Layout ---
        central = QWidget()
        layout = QGridLayout(central)

        layout.setContentsMargins(20, 20, 20, 20)
        layout.setHorizontalSpacing(20)
        layout.setVerticalSpacing(20)

        # --- Oscilloscope container ---
        osc_container = QWidget()
        osc_layout = QGridLayout(osc_container)
        osc_layout.setContentsMargins(10, 10, 14, 10)
        osc_layout.setSpacing(0)

        # Oskilloskooppi täyttää solun
        osc_layout.addWidget(self.osc, 0, 0)

        # Numeerinen näyttö oikeaan alakulmaan
        osc_layout.addWidget(
            self.current_display,
            10,
            0,
            Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter,
        )

        layout.addWidget(osc_container, 0, 0)
        layout.addWidget(self.result_indicator, 1, 0)
        layout.addWidget(self.start_button, 0, 1)
        layout.addWidget(self.cancel_button, 1, 1)
        layout.addWidget(self.stop_button, 2, 1)
        layout.addWidget(self.footer, 3, 0, 1, 2)

        self.setCentralWidget(central)

    # ----------------------------------------------------
    # START pressed → run test in thread
    # ----------------------------------------------------
    def _on_start(self):
        print("DEBUG: START pressed")

        if self.thread is not None and self.thread.isRunning():
            print("DEBUG: Test already running, ignoring START")
            return

        # UI state
        self.start_button.set_running()
        self.logic.update_status("Running")

        # Reset flags
        self.test_runner.cancel_requested = False
        self.test_runner.stop_requested = False

        # Thread + worker
        self.thread = QThread()
        self.worker = TestWorker(self.test_runner)
        self.worker.moveToThread(self.thread)

        # Signals
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self._on_test_finished)
        self.worker.aborted.connect(self._on_test_aborted)

        # Cleanup
        self.worker.finished.connect(self.thread.quit)
        self.worker.aborted.connect(self.thread.quit)
        self.thread.finished.connect(self._on_thread_finished)

        self.thread.start()

    # ----------------------------------------------------
    # Test finished normally
    # ----------------------------------------------------
    def _on_test_finished(self, value, result):
        print("DEBUG: test finished")

        self.osc.set_value(value)
        self.current_display.update_value(value)  # <<< UPDATE DISPLAY
        self.result_indicator.set_state(result.lower())
        self.start_button.set_ready()

        self.logic.update_status("Finished")

    # ----------------------------------------------------
    # Test aborted
    # ----------------------------------------------------
    def _on_test_aborted(self):
        print("DEBUG: test aborted")

        self.result_indicator.set_state("fail")
        self.start_button.set_ready()

        self.logic.update_status("Aborted")

    # ----------------------------------------------------
    # Thread finished
    # ----------------------------------------------------
    def _on_thread_finished(self):
        print("DEBUG: thread finished")
        self.thread = None
        self.worker = None

    # ----------------------------------------------------
    # CANCEL
    # ----------------------------------------------------
    def _on_cancel(self):
        print("DEBUG: CANCEL pressed")
        self.logic.cancel_pressed()

    # ----------------------------------------------------
    # STOP
    # ----------------------------------------------------
    def _on_stop(self):
        print("DEBUG: STOP pressed")
        self.logic.stop_pressed()
        self.result_indicator.set_state("fail")
        self.start_button.set_ready()

    # ----------------------------------------------------
    # Window close
    # ----------------------------------------------------
    def closeEvent(self, event):
        if self.thread is not None and self.thread.isRunning():
            try:
                self.test_runner.request_stop()
            except Exception:
                pass
            try:
                self.thread.quit()
                self.thread.wait(3000)
            except Exception:
                pass

        super().closeEvent(event)
