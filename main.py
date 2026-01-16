# ----------------------------------------------
# Project ProductionTester
# V0.9.12
# main.py
# Copyright BigJ
# 11.01.2026
# ----------------------------------------------

import sys

from PyQt6.QtWidgets import QApplication

from UI.main_window import MainWindow


def main():
    app = QApplication(sys.argv)

    # Lataa QSS-tyyli
    with open("UI/style.qss", "r") as f:
        app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
