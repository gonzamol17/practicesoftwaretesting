import json
import time

from POM.HeaderMenuPage import HeaderMenuPage
from POM.LoginPage import LoginPage
from POM.MyAccountPage import MyAccountPage
from Utils.BaseClass import BaseClass


class TestVerifyCategoriesItems(BaseClass):

      def test_VerifyCategoriesItems(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        hmp = HeaderMenuPage(driver)
        hmp.selectLinkCategories()
        categoriesExpected = ['Hand Tools', 'Power Tools', 'Other', 'Special Tools', 'Rentals']
        categoriesActual = hmp.verifyAllTheCategoriesItems()
        assert categoriesActual == categoriesExpected
        #assert sorted(categoriesActual) == sorted(categoriesExpected1)
        time.sleep(3)
