# ----------------------------------------------
# Project ProductionTester
# V0.1
# interfaces/product_interface.py
# Copyright BigJ
# 10.08.2026
# ----------------------------------------------

from abc import ABC, abstractmethod

class ProductInterface(ABC):

    @abstractmethod
    def get_expected_current_mA(self) -> float:
        """Return the product's nominal current consumption."""
        pass