import json
import time

from POM.HomePage import HomePage
from Utils.BaseClass import BaseClass


class TestVerifyTheMoveOver_SliderPrice(BaseClass):

      def test_VerifyTheMoveOver_SliderPrice(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        expectedSliderValues = ['1', '100']
        actualSliderValues = hp.verifyMinAndMaxPriceOverSlider()
        assert len(expectedSliderValues) == len(actualSliderValues)
        assert expectedSliderValues == actualSliderValues
        driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(3)
        minSliderValue = 57
        maxSliderValue = 157
        hp.doMoveFromMinAndMaxSlider(minSliderValue, maxSliderValue)
        expectedPrices = ['0', '200']
        actualPrices = hp.showMeMinPriceStatus()
        assert len(expectedPrices) == len(actualPrices)
        assert expectedPrices == actualPrices
        time.sleep(3)
