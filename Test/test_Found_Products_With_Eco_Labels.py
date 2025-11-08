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
        eco_products, total_eco = hp.showMeEachElementIfExistEcoLabel()
        assert total_eco > 0, "No se encontraron productos con label ECO"
        print(f"\n🌿 Total de productos ECO encontrados en todas las páginas: {total_eco}")
        time.sleep(3)
