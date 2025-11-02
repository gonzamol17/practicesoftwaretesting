import json
import time

import faker

from POM.CheckoutPage import CheckoutPage
from POM.HeaderMenuPage import HeaderMenuPage
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage
from POM.MyAccountPage import MyAccountPage
from POM.MyFavoritePage import MyFavoritePage
from POM.MyInvoicesPage import MyInvoicesPage
from POM.MyProfilePage import MyProfilePage
from POM.ProductDetailPage import ProductDetailPage
from Utils.BaseClass import BaseClass
from faker import Faker


class TestVerifyAfterPaymentTheOrderWasCreated(BaseClass):

      def test_VerifyAfterPaymentTheOrderWasCreated(self):
          log = self.get_Logger()
          log.info("Se está por loguear en la página")
          driver = self.driver
          hmp = HeaderMenuPage(driver)
          hmp.selectLinkSignIn()
          fake = Faker()
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
          productName = "Thor Hammer"
          hp.selectAParticularElementFromPaginationComponent(productName)
          time.sleep(3)
          pdp = ProductDetailPage(driver)
          time.sleep(1)
          pdp.selectTheAddToCartBtn()
          time.sleep(2)
          hmp.selectShoppingCartItem()
          time.sleep(1)
          chp = CheckoutPage(driver)
          chp.selectTheCheckoutBtn()
          time.sleep(1)
          chp.selectTheSecondCheckoutBtn()
          time.sleep(1)
          chp.selectTheThirdCheckoutBtn()
          time.sleep(1)
          chp.selectThePaymentMethodValue("Credit Card")
          time.sleep(1)
          raw_card_number = fake.credit_card_number(card_type='visa')
          # Darle formato tipo 4970-1100-0000-0062
          formatted_card_number = '-'.join([raw_card_number[i:i + 4] for i in range(0, len(raw_card_number), 4)])
          chp.completeActionToPayment(formatted_card_number, fake.credit_card_expire(date_format='%m/%Y') , fake.random_int(min=100, max=999),  fake.name())
          assert "Payment was successful" == chp.getSuccessfullMsgPaymentConfirmed()
          assert chp.verifyIfBtnConfirmArePresent() == True
          time.sleep(1)
          chp.selectTheLastBtnConfirm()
          time.sleep(1)
          assert "Thanks for your order!" in chp.getOrderInvoiceConfirmed()
          txtInvoice = chp.getOrderInvoiceConfirmed()
          expectedInvoice = chp.getInvoiceNumber(txtInvoice)
          hmp.selectLogoToRedirectHomePage()
          hmp.selectMyAccountNameOption()
          hmp.selectMyInvoicesOption()
          mip = MyInvoicesPage(driver)
          actualInvoice = mip.showMeMyLastInvoice()
          assert expectedInvoice == actualInvoice
          time.sleep(6)




