import json
import time

from POM.HeaderMenuPage import HeaderMenuPage
from POM.LoginPage import LoginPage
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.ProductDetailPage import ProductDetailPage

class TestVerifyTheCo2Category(BaseClass):

      def test_VerifyTheCo2CategoryForAProduct(self):
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
          lp.completeSignInAction(email, password)
          hp = HomePage(driver)
          time.sleep(1)
          hmp.selectLogoToRedirectHomePage()
          searchedProduct = "Belt Sander"
          # CO2 del card
          co2_from_card = hp.findProductAndGetCo2FromCard(searchedProduct)
          pdp = ProductDetailPage(driver)
          # CO2 del detalle
          co2_from_detail = pdp.getCo2FromDetail()
          assert co2_from_card == co2_from_detail
