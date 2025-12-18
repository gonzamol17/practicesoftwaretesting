import json
import time

from POM.HomePage import HomePage
from POM.ProductDetailPage import ProductDetailPage
from Utils.BaseClass import BaseClass


class TestVerifyForOutOfStockProductYouCantAddToCart(BaseClass):

      def test_VerifyForOutOfStockProductYouCantAddToCart(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        hp = HomePage(driver)
        productOutOfStock = hp.findFirstOutOfStockProduct()
        pdp = ProductDetailPage(driver)
        pdp.selectTheOutOfStockProduct(productOutOfStock)
        assert pdp.getLabelOutOfStock() == "Out of stock"
        assert pdp.showStatusOfBtnAddToCart()
        time.sleep(2)
