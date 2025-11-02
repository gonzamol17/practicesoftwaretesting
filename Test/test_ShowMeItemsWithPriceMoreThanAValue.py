import json
import time

from POM.HomePage import HomePage
from POM.ResultPage import ResultPage
from Utils.BaseClass import BaseClass


class TestShowMeItemsWithPriceMoreThanAValue(BaseClass):

      def test_ShowMeItemsWithPriceMoreThanAValue(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        hp = HomePage(driver)
        actualListHammerItemsMore14 = [('Sledgehammer', 17.75), ('Claw Hammer with Fiberglass Handle', 20.14), ('Court Hammer', 18.63)]
        productName = "Hammer"
        hp.doASearchProduct(productName)
        time.sleep(3)
        rp = ResultPage(driver)
        valuePrice = 14.0
        priceListExpected = rp.showTheItemsForPricesMoreThanAValue(valuePrice)
        print(priceListExpected)
        assert actualListHammerItemsMore14 == priceListExpected
