import json
import time

from POM.HeaderMenuPage import HeaderMenuPage
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage
from POM.ProductDetailPage import ProductDetailPage
from POM.CheckoutPage import CheckoutPage
from Utils.BaseClass import BaseClass


class TestVerifyTotalPriceFromFromCheckoutPage(BaseClass):

      def test_VerifyTotalPriceFromCheckoutPage(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        hmp = HeaderMenuPage(driver)
        hmp.selectLinkSignIn()
        time.sleep(1)
        file = open("..\\Data\\Login.json", "r")
        jsondata = file.read()
        obj = json.loads(jsondata)
        list = obj['users']
        email = list[0].get("email")
        password = list[0].get("password")
        lp = LoginPage(driver)
        time.sleep(1)
        lp.completeSignInAction(email, password)
        time.sleep(1)
        hmp.selectLogoToRedirectHomePage()
        time.sleep(1)
        hp = HomePage(driver)
        time.sleep(1)
        productName = "Mini Screwdriver"
        hp.selectAParticularElementFromPaginationComponent(productName)
        time.sleep(3)
        pdp = ProductDetailPage(driver)
        priceProduct = pdp.getIndividualProductPrice()
        #print(priceProduct)
        time.sleep(1)
        pdp.selectTheAddToCartBtn()
        time.sleep(5)
        hmp.selectShoppingCartItem()
        time.sleep(1)
        chp = CheckoutPage(driver)
        priceFromCheckout = chp.getIndividualProductPriceFromCheckout()[1:]
        assert priceProduct == priceFromCheckout
        #print(priceFromCheckout)
        time.sleep(3)



