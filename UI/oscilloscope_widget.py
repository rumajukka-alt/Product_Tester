# ----------------------------------------------
# Project ProductionTester
# V0.1
# UI/oscilloscope_widget.py
# Copyright BigJ
# 10.08.2026
# ----------------------------------------------

from PyQt6.QtWidgets import QWidget, QSizePolicy
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6.QtCore import Qt


class OscilloscopeWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Näytön koko- ja kuvasuhderajoitukset
        self.setMinimumWidth(600)     # estää kärpäsen paska -efektin
        self.setMaximumWidth(850)     # sinun asettama arvo
        self.setMaximumHeight(350)    # sinun asettama arvo
        
        # Mittausarvo ja rajat
        self.current_value = None
        self.min_limit = None
        self.max_limit = None
      
        
    def set_limits(self, min_limit, max_limit):
        self.min_limit = min_limit
        self.max_limit = max_limit
        self.update()
        
        # Layout-käyttäytyminen
        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )

    def resizeEvent(self, event):
        # Pakotetaan kuvasuhde 16:9
        w = self.width()
        h = int(w * 9 / 16)

        # Ei ylitetä maksimikorkeutta
        if h > self.maximumHeight():
            h = self.maximumHeight()

        self.setFixedHeight(h)
        super().resizeEvent(event)

    def set_value(self, value):
        self.current_value = value
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), self.palette().window())

        w = self.width()
        h = self.height()


        # Ei speksirajoja → ei piirretä mitään
        if self.min_limit is None or self.max_limit is None:
            return

        # Speksirajat
        painter.setPen(QPen(QColor(255, 0, 0), 2))
        y_min = h - (self.min_limit * h / 40)
        y_max = h - (self.max_limit * h / 40)
        painter.drawLine(0, int(y_min), w, int(y_min))
        painter.drawLine(0, int(y_max), w, int(y_max))

        # Mitattu arvo
        if self.current_value is not None:
            painter.setPen(QPen(QColor(0, 255, 0), 3))
            y_val = h - (self.current_value * h / 40)
            painter.drawLine(0, int(y_val), w, int(y_val))