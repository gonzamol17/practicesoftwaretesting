import json
import time

from POM.ForgotPasswordPage import ForgotPasswordPage
from POM.HeaderMenuPage import HeaderMenuPage
from POM.LoginPage import LoginPage
from Utils.BaseClass import BaseClass


class TestRecoverForgotPassword_Failure(BaseClass):

      def test_RecoverForgotPassword_Failure(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        hmp = HeaderMenuPage(driver)
        hmp.selectLinkSignIn()
        lp = LoginPage(driver)
        lp.selectForgotPasswordOption()
        fpp = ForgotPasswordPage(driver)
        assert fpp.showMainTitleForgotPassword() == "Forgot Password"
        wrongEmail = "pedro@gmail.com"
        fpp.doRecoverPasswordAction(wrongEmail)
        assert fpp.showMsgError() == "The selected email is invalid. "
        time.sleep(2)
