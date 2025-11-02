import json
import time

from selenium.common import NoSuchElementException

from POM.CheckoutPage import CheckoutPage
from POM.HeaderMenuPage import HeaderMenuPage
from POM.HomePage import HomePage
from POM.ProductDetailPage import ProductDetailPage
from Utils.BaseClass import BaseClass


class TestCleanTheShoppingCart(BaseClass):

      def test_CleanTheShoppingCart(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        hp = HomePage(driver)
        hmp = HeaderMenuPage(driver)
        pdp = ProductDetailPage(driver)
        time.sleep(1)
        productName = "Combination Pliers"
        hp.selectAParticularElementFromPaginationComponent(productName)
        pdp.selectTheAddToCartBtn()
        time.sleep(1)
        hmp.selectLogoToRedirectHomePage()
        time.sleep(1)
        productName1 = "Pliers"
        hp.selectAParticularElementFromPaginationComponent(productName1)
        pdp.selectTheAddToCartBtn()
        time.sleep(1)
        hmp.selectLogoToRedirectHomePage()
        time.sleep(1)
        cp = CheckoutPage(driver)
        shoppingCartIcon = hmp.verifyIfShoppingCartIsPresent()
        if shoppingCartIcon:
            time.sleep(1)
            hmp.selectShoppingCartItem()
            time.sleep(1)
            cp.cleanShoppingCart()
        time.sleep(1)
        hmp.selectLogoToRedirectHomePage()
        assert hmp.verifyIfShoppingCartIsPresent() is False
        print("No hay productos agregados al Carrito de compras, por eso no se visualiza")
        time.sleep(2)
