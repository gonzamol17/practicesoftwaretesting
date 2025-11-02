import json
import time

import pytest

from POM.HeaderMenuPage import HeaderMenuPage
from POM.LoginPage import LoginPage
from POM.MyAccountPage import MyAccountPage
from Utils.BaseClass import BaseClass

@pytest.mark.smoke
class TestLoginValidationError(BaseClass):

      def test_LoginValidationError(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        hmp = HeaderMenuPage(driver)
        hmp.selectLinkSignIn()
        lp = LoginPage(driver)
        lp.selectBtnLogin()
        time.sleep(1)
        assert lp.showEmailErrorValidationLogin() == "Email is required"
        assert lp.showPassErrorValidationLogin() == "Password is required"
        assert lp.showEmailColorErrorField() == "rgb(220, 53, 69)"
        assert lp.showPassColorerrorField() == "rgb(220, 53, 69)"
        time.sleep(2)
