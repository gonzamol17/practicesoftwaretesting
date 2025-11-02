import json
import time

from POM.HomePage import HomePage
from Utils.BaseClass import BaseClass


class TestVerifyNoResultsMessage(BaseClass):

      def test_VerifyNoResultsMessage(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        productName = "no products"
        hp.doASearchProduct(productName)
        assert productName in hp.showMeResultTitle()
        assert "There are no products found." == hp.showMeResultSubTitle()
        time.sleep(3)
