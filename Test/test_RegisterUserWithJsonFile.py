import json
import time

import pytest
from selenium.webdriver.common.by import By

from POM.HeaderMenuPage import HeaderMenuPage
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage
from POM.RegistrationPage import RegistrationPage
from Utils.BaseClass import BaseClass


class TestRegisterUserWithJsonFile(BaseClass):

      def test_RegisterUserWithJsonFile(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        hmp = HeaderMenuPage(driver)
        time.sleep(3)
        hmp.selectLinkSignIn()
        lp = LoginPage(driver)
        lp.selectRegisterLinkOption()
        rp = RegistrationPage(driver)
        file1 = open("..\\Data\\Register.json", "r")
        jsondata1 = file1.read()
        obj1 = json.loads(jsondata1)
        list1 = obj1['users']
        n = 0
        rp.completeRegisterForm(list1[n].get("firstName"), list1[n].get("lastName"), list1[n].get("dateBirth"), list1[n].get("address"),
                                list1[n].get("postCode"), list1[n].get("city"), list1[n].get("state"), list1[n].get("country"),
                                list1[n].get("phone"), list1[n].get("emailAddress"), list1[n].get("password"))

        assert lp.showLoginTitle() == "Login"
        time.sleep(3)


