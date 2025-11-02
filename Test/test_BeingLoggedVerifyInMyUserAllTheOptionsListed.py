import json
import time

from POM.HeaderMenuPage import HeaderMenuPage
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage
from POM.MyAccountPage import MyAccountPage
from Utils.BaseClass import BaseClass


class TestBeingLoggedVerifyFromMyUserAllOptionsListed(BaseClass):

      def test_BeingLoggedVerifyFromMyUserAllOptionsListed(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        hmp = HeaderMenuPage(driver)
        hmp.selectLinkSignIn()
        elementsFromMyAccountNameExpected = ['My account', 'My favorites', 'My profile', 'My invoices', 'My messages', 'Sign out']
        time.sleep(1)
        file = open("..\\Data\\Login.json", "r")
        jsondata = file.read()
        obj = json.loads(jsondata)
        list = obj['users']
        email = list[0].get("email")
        password = list[0].get("password")
        lp = LoginPage(driver)
        lp.completeSignInAction(email, password)
        time.sleep(1)
        hmp.selectLogoToRedirectHomePage()
        time.sleep(1)
        hmp.selectMyAccountNameOption()
        time.sleep(1)
        elementsFromMyAccountActual = hmp.showMeListFromMyAccountName()
        assert elementsFromMyAccountNameExpected == elementsFromMyAccountActual
        print("Al seleccionar My Account Name, los subelemntos mostrados son: \n" + "\n".join(elementsFromMyAccountActual))
        time.sleep(1)
