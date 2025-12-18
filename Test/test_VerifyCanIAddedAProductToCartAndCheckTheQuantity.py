import time
from POM.HomePage import HomePage
from POM.ProductDetailPage import ProductDetailPage
from Utils.BaseClass import BaseClass

class TestVerifyCanIAddedAProductToCartAndCheckTheQuantity(BaseClass):

      def test_VerifyCanIAddedAProductToCartAndCheckTheQuantity(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        hp = HomePage(driver)
        productName = "Tool Cabinet"
        hp.selectAParticularElementFromPaginationComponent(productName)
        pdp = ProductDetailPage(driver)
        numberOfIncrease = 3
        pdp.increaseQuantityProduct(numberOfIncrease)
        time.sleep(1)
        assert pdp.verifyTheGreenBannerIsPresented() == "Product added to shopping cart."
        quantity = int(pdp.verifyTheQuantityFromCartIcon())
        assert numberOfIncrease == quantity
        print(f'La cantidad del producto seleccionado es {quantity}')
        time.sleep(2)
