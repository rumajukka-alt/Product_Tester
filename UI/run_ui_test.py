# ----------------------------------------------
# Project ProductionTester
# V0.1
# UI/run_ui_test.py
# NOT A PRODUCTION CODE made for testing
# Copyright BigJ
# 10.08.2026
# ----------------------------------------------

# DEBUG

import sys

from PyQt6.QtWidgets import QApplication

from UI.main_window import MainWindow


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
