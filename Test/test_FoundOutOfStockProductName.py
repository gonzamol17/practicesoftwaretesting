import json
import time

from POM.HomePage import HomePage
from Utils.BaseClass import BaseClass


class TestFoundOutOfStockProductName(BaseClass):

      def test_FoundOutOfStockProductName(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        hp = HomePage(driver)
        status = hp.showMeEachElementIfExistOutOfStockProduct()
        if status:
          for product in status:
            log.info(f"Producto fuera de stock: {product['nombre']} (Página {product['pagina']})")
        else:
          log.info("No hay productos fuera de stock")

        assert len(status) > 0, "❌ No se encontró ningún producto 'Out of stock'."
        time.sleep(3)
