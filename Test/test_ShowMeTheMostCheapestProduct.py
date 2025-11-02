import json
import time

from POM.HomePage import HomePage
from POM.ResultPage import ResultPage
from Utils.BaseClass import BaseClass


class TestShowMeTheMostCheapestProduct(BaseClass):

      def test_ShowMeTheMostCheapestProduct(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        hp = HomePage(driver)
        minPrice, name = hp.giveMeTheMostCheapestProductFromTable()
        assert minPrice == 3.55
        assert name == "Washers"
        print(f"Producto con el minimo precio es: {name} y es de ${minPrice}")
        time.sleep(3)
