import json
import time

import pytest

from POM.ResultPage import ResultPage
from POM.HomePage import HomePage
from Utils.BaseClass import BaseClass


class TestSortAscendingAlphabeticalOrder(BaseClass):
      @pytest.mark.smoke
      def test_SortAscendingAlphabeticalOrder(self):
        log = self.get_Logger()
        log.info("Sort Ascending Alphabetical Order")
        expectedOrderProductList = ['Adjustable Wrench', 'Angled Spanner', 'Belt Sander', 'Bolt Cutters', 'Chisels Set', 'Circular Saw', 'Claw Hammer', 'Claw Hammer with Fiberglass Handle', 'Claw Hammer with Shock Reduction Grip']
        driver = self.driver
        rp = ResultPage(driver)
        time.sleep(1)
        originalOrder = rp.showTheListOfWantedProducts()
        print(originalOrder)
        hp = HomePage(driver)
        time.sleep(1)
        sort = "Name (A - Z)"
        hp.selectFilterToSortProducts(sort)
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 300)")
        modifiedOrder = rp.showTheListOfWantedProducts()
        assert modifiedOrder == expectedOrderProductList
        print(modifiedOrder)
        time.sleep(1)


