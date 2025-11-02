import json
import time

from POM.HeaderMenuPage import HeaderMenuPage
from POM.LoginPage import LoginPage
from POM.MyAccountPage import MyAccountPage
from Utils.BaseClass import BaseClass


class TestVerifyMyAccount_Elements(BaseClass):

      def test_VerifyMyAccount_Elements(self):
        log = self.get_Logger()
        driver = self.driver
        hmp = HeaderMenuPage(driver)
        time.sleep(3)
        hmp.selectLinkSignIn()
        file = open("..\\Data\\Login.json", "r")
        jsondata = file.read()
        obj = json.loads(jsondata)
        list = obj['users']
        email = list[0].get("email")
        password = list[0].get("password")
        lp = LoginPage(driver)
        lp.completeSignInAction(email, password)
        map = MyAccountPage(driver)
        itemsExpected = [" Favorites", " Profile", " Invoices", " Messages"]
        itemsActual = map.showMyAccountItems()
        print(itemsActual)
        assert itemsActual == itemsExpected
        print("La lista obtenida es igual a la esperada")
        time.sleep(3)
