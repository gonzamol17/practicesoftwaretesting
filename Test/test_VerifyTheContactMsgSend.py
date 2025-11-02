import json
import time

import pytest

from POM.ContactPage import ContactPage
from POM.HeaderMenuPage import HeaderMenuPage
from POM.LoginPage import LoginPage
from POM.MessagesPage import MessagePage
from POM.MyAccountPage import MyAccountPage
from Utils.BaseClass import BaseClass


class TestVerifyTheContactMsgSend(BaseClass):

      def test_VerifyTheContactMsgSend(self):
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
        time.sleep(1)
        hmp.selectContactOption()
        cp = ContactPage(driver)
        subject = "Payments"
        msg = "This is the first message complete to send just to see if is abel to complete the text box area"
        cp.completeTheFormContact(subject, msg)
        assert cp.showConfirmMsg() == "Thanks for your message! We will contact you shortly."
        hmp.selectMyAccountNameOption()
        hmp.selectMyMessagesOption()
        mp = MessagePage(driver)
        assert mp.showMeSubject() == subject
        assert msg.startswith((mp.showMeMsg().rstrip("...")))
        assert mp.showMeStatus() == "NEW"
        time.sleep(1)
        mp.selectBtnMoreDetails()
        time.sleep(1)
        assert mp.getDetailsOfMsg() == msg
        time.sleep(3)
