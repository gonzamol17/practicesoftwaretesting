import json
import time

from POM.HomePage import HomePage
from POM.ResultPage import ResultPage
from Utils.BaseClass import BaseClass


class TestSearchHammerProductAndGetTotalPrice(BaseClass):

      def test_SearchHammerProductAndGetTotalPrice(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        hp = HomePage(driver)
        productName = "Hammer"
        hp.doASearchProduct(productName)
        time.sleep(3)
        rp = ResultPage(driver)
        assert rp.showThePricesForWantedProducts() == 105.13
