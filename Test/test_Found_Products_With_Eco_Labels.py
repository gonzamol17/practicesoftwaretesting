import json
import time

from POM.HomePage import HomePage
from Utils.BaseClass import BaseClass


class TestFoundProductsWithEcoLabels(BaseClass):

      def test_FoundProductsWithEcoLabels(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        hp = HomePage(driver)
        eco_products = hp.showMeEachElementIfExistEcoLabel()
        assert len(eco_products) > 0, "❌ No se encontraron productos con label ECO."
        print("\nProductos ECO encontrados:")
        for p in eco_products:
          print(f"🌿 {p}")
