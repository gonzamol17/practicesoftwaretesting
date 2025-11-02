import json
import time

import pytest

from POM.HeaderMenuPage import HeaderMenuPage
from POM.LoginPage import LoginPage
from POM.MyAccountPage import MyAccountPage
from Utils.BaseClass import BaseClass


class TestLogin_Successfull(BaseClass):

      def test_Login_Successfull(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
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
        assert map.showMeMyAccountTitle() == "My account"
        time.sleep(3)
