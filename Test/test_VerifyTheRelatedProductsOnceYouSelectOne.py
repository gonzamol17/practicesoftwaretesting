import json
import time

from POM.HomePage import HomePage
from POM.ProductDetailPage import ProductDetailPage
from Utils.BaseClass import BaseClass


class TestVerifyTheRelatedProductsOnceYouSelectOne(BaseClass):

      def test_VerifyTheRelatedProductsOnceYouSelectOne(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.selectOneProductFromCard()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 300)")
        pdp = ProductDetailPage(driver)
        assert pdp.verifyIfRelatedProductTitleIsPresented() == "Related products"
        total = pdp.checkTheNumberOfRelatedProducts()
        assert total == 4
        print(f"El total de elementos visualizados en la sección Related Products es: {total}")
        time.sleep(3)
