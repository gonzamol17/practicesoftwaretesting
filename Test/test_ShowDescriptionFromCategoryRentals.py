import json
import time

from POM.RentalsPage import RentalsPage
from POM.HeaderMenuPage import HeaderMenuPage
from Utils.BaseClass import BaseClass


class TestShowDescriptionFromCategoryRentals(BaseClass):

      def test_ShowDescriptionFromCategoryRentals(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        hmp = HeaderMenuPage(driver)
        categorySelected = "Rentals"
        searchItem = "Excavator"
        hmp.selectLinkCategories()
        time.sleep(1)
        hmp.selectAParticularCategory(categorySelected)
        time.sleep(1)
        rp = RentalsPage(driver)
        description = rp.showMeTheDescriptionForAParticularProduct(searchItem)
        print(description)
        assert "Aliquam tempus consequat ligula rutrum consequat" in description
        time.sleep(2)
