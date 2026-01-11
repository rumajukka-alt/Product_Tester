# ----------------------------------------------
# Project ProductionTester
# V0.2
# main.py
# Copyright BigJ
# 10.08.2026
# ----------------------------------------------

from PyQt6.QtWidgets import QApplication
import sys
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
