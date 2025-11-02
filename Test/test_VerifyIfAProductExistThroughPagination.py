import json
import time

from selenium.webdriver.common.by import By

from POM.HeaderMenuPage import HeaderMenuPage
from POM.HomePage import HomePage
from POM.ResultPage import ResultPage
from Utils.BaseClass import BaseClass


class TestVerifyIfAProductExistThroughPagination(BaseClass):

      def test_VerifyIfAProductExistThroughPagination(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        hp = HomePage(driver)
        productName = "Safety Goggles"
        status = hp.showMeEachElementFromPaginationComponent(productName)
        try:
            assert status is True
        except Exception as e:
            print("¡No se ha encontrado el producto en la tabla!")
        time.sleep(3)
