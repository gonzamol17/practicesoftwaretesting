import json
import time

from POM.HomePage import HomePage
from Utils.BaseClass import BaseClass


class TestShowMeTotalPriceFromFivePages(BaseClass):

      def test_ShowMeTotalPriceFromFivePages(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        hp = HomePage(driver)
        totPrice = hp.giveMeTotalPriceFromEachProductFromFivePages()
        assert totPrice == 1208.54
        print(f"La suma total de todos los precios listados es: ${totPrice}")
        time.sleep(3)
