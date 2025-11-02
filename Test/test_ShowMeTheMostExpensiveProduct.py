import json
import time

from POM.HomePage import HomePage
from POM.ResultPage import ResultPage
from Utils.BaseClass import BaseClass


class TestShowMeTheMostExpensiveProduct(BaseClass):

      def test_ShowMeTheMostExpensiveProduct(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        hp = HomePage(driver)
        maxPrice, name = hp.giveMeTheMostExpensiveProductFromTable()
        assert maxPrice == 89.55
        assert name == "Drawer Tool Cabinet"
        print(f"Producto con el máximo precio es: {name} y es de ${maxPrice}")
        time.sleep(3)
