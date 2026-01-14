import json
import time

import faker

from POM.CheckoutPage import CheckoutPage
from POM.HeaderMenuPage import HeaderMenuPage
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage
from POM.MyAccountPage import MyAccountPage
from POM.MyFavoritePage import MyFavoritePage
from POM.MyProfilePage import MyProfilePage
from POM.ProductDetailPage import ProductDetailPage
from Utils.BaseClass import BaseClass


class TestVerifyQtyAndTotalAmount(BaseClass):

      def test_VerifyQtyAndTotalAmount(self):
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
          result = hmp.cleanShoppingCartItem()
          if result == False:
              cp = CheckoutPage(driver)
              cp.cleanShoppingCart()
          time.sleep(1)
          hp = HomePage(driver)
          productName = "Chisels Set"
          hp.selectAParticularElementFromPaginationComponent(productName)
          pdp = ProductDetailPage(driver)
          qtyNumber = 3
          pdp.insertQtyNumber(qtyNumber)
          pdp.addQtyNumberToTheCart()
          time.sleep(1)
          hmp.selectShoppingCartItem()
          chp = CheckoutPage(driver)
          assert qtyNumber == chp.showMeQty()
          individual_price = chp.showMeIndividualPrice()
          total_price = individual_price * qtyNumber
          assert chp.showMeTotalPrice() == total_price
          time.sleep(2)