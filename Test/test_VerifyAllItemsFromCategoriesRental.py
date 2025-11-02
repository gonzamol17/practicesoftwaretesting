import json
import time

from POM.RentalsPage import RentalsPage
from POM.HeaderMenuPage import HeaderMenuPage
from Utils.BaseClass import BaseClass


class TestVerifyAllItemsFromCategoriesRental(BaseClass):

      def test_VerifyAllItemsFromCategoriesRental(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        hmp = HeaderMenuPage(driver)
        categorySelected = "Rentals"
        itemsExpected = ['Excavator', 'Bulldozer', 'Crane']
        hmp.selectLinkCategories()
        hmp.selectAParticularCategory(categorySelected)
        rp = RentalsPage(driver)
        items = rp.showTheListOfWantedProducts()
        assert items == itemsExpected
        time.sleep(2)
