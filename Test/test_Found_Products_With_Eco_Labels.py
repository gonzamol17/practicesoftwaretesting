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
        all_products = hp.showMeEachElementIfExistEcoLabel()
        print(f"\nTotal de productos encontrados: {len(all_products)}")
        time.sleep(3)
