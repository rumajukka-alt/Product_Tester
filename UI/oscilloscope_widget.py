# ----------------------------------------------
# Project ProductionTester
# V0.1
# UI/oscilloscope_widget.py
# Copyright BigJ
# 11.01.2026
# ----------------------------------------------

from PyQt6.QtCore import QRectF, Qt
from PyQt6.QtGui import QColor, QFont, QFontMetrics, QPainter, QPen
from PyQt6.QtWidgets import QSizePolicy, QWidget


class OscilloscopeWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("oscilloscope_widget")  # <<< TÄMÄ

        # Näytön koko- ja kuvasuhderajoitukset
        self.setMinimumWidth(600)  # estää kärpäsen paska -efektin
        self.setMaximumWidth(850)  # sinun asettama arvo
        self.setMaximumHeight(350)  # sinun asettama arvo
        # Aseta koko-käyttäytyminen heti niin layout osaa varata tilan
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)

        # Mittausarvo ja rajat
        self.current_value = None
        self.min_limit = None
        self.max_limit = None

    def set_limits(self, min_limit, max_limit):
        self.min_limit = min_limit
        self.max_limit = max_limit
        self.update()

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
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        w = self.width()
        h = self.height()

        # Piirretään pyöristetty tausta ja leveä reunus aina
        bg_color = QColor(30, 30, 30, 230)
        border_color = QColor(80, 160, 220)  # selkeä mutta ei-valkoinen
        border_width = 6
        radius = min(w, h) * 0.06

        rect = QRectF(
            border_width / 2, border_width / 2, w - border_width, h - border_width
        )
        painter.setPen(QPen(border_color, border_width))
        painter.setBrush(bg_color)
        painter.drawRoundedRect(rect, radius, radius)

        # Jos speksirajoja ei ole, piirrämme vain taustan ja kehykset
        if self.min_limit is None or self.max_limit is None:
            return

        # Speksirajat — käytetään dynaamista skaalausta niin, ettei kaikki osu
        # pienelle alueelle y-akselilla. Lisätään pieni padding ja min-span.
        painter.setPen(QPen(QColor(255, 0, 0), 2))

        # Laske näyttöön tuleva min/max (lisää paddingia jos span on pieni)
        spec_min = float(self.min_limit)
        spec_max = float(self.max_limit)
        span = spec_max - spec_min
        min_span = 0.5  # mA, pienin näyttöspanna
        if span < min_span:
            # Jos rajat ovat liian lähellä, laajennetaan niiden väliä symmetrisesti
            extra = (min_span - span) / 2.0 + 0.1
            display_min = spec_min - extra
            display_max = spec_max + extra
        else:
            padding = span * 0.15  # 15% padding molemmin puolin
            display_min = spec_min - padding
            display_max = spec_max + padding

        # Varmista, ettei display-span ole nolla
        display_span = display_max - display_min
        if display_span == 0:
            display_span = 1.0

        # Varaamme vasemman marginaalin y-asteikon tekstiä varten
        left_margin = 60

        plot_x0 = left_margin
        plot_x1 = w - int(border_width)

        def map_y(val: float) -> int:
            # Normalize and invert for Qt coordinate system inside plot area
            norm = (val - display_min) / display_span
            norm = max(0.0, min(1.0, norm))
            return int(h - norm * h)

        y_min = map_y(self.min_limit)
        y_max = map_y(self.max_limit)
        painter.drawLine(plot_x0, int(y_min), plot_x1, int(y_min))
        painter.drawLine(plot_x0, int(y_max), plot_x1, int(y_max))

        # Mitattu arvo
        if self.current_value is not None:
            painter.setPen(QPen(QColor(0, 255, 0), 3))
            y_val = map_y(self.current_value)
            painter.drawLine(plot_x0, int(y_val), plot_x1, int(y_val))

        # --- Piirrä y-akselin asteikko ja tickit vasemmalle
        painter.setPen(QPen(QColor(200, 200, 200), 1))
        font = QFont("Arial", 10)
        painter.setFont(font)
        fm = QFontMetrics(font)

        # Valitse noin 5 tikkiä
        ticks = 5
        for i in range(ticks):
            tval = display_min + (display_span * i) / (ticks - 1)
            ty = map_y(tval)
            # Tick - pieni viiva plotin reunaan
            painter.drawLine(plot_x0 - 6, ty, plot_x0, ty)
            label = f"{tval:.2f}"
            text_w = fm.horizontalAdvance(label)
            text_h = fm.ascent()
            painter.drawText(plot_x0 - 8 - text_w, ty + text_h // 2, label)
