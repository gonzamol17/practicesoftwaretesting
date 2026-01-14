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
          hp = HomePage(driver)
          productName = "Thor Hammer"
          hp.selectAParticularElementFromPaginationComponent(productName)
          pdp = ProductDetailPage(driver)
          qtyNumber = 2
          pdp.insertQtyNumber(qtyNumber)
          pdp.addQtyNumberToTheCart()
          assert "You can only have one" in pdp.getToastMessage()
          time.sleep(6)