import json
import time

from POM.HeaderMenuPage import HeaderMenuPage
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage
from POM.MyAccountPage import MyAccountPage
from POM.MyFavoritePage import MyFavoritePage
from POM.MyProfilePage import MyProfilePage
from POM.ProductDetailPage import ProductDetailPage
from Utils.BaseClass import BaseClass


class TestVerifyTheUpdatedAddressFromMyProfile(BaseClass):

      def test_VerifyTheUpdatedAddressFromMyProfile(self):
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
        mfp = MyFavoritePage(driver)
        lp.completeSignInAction(email, password)
        time.sleep(1)
        hmp.selectMyAccountNameOption()
        time.sleep(1)
        hmp.selectAParticularCategory("My profile")
        mpp = MyProfilePage(driver)
        newStreet = "Los Manzanos"
        newCountry = "Penalpas"
        time.sleep(1)
        mpp.updateAddress(newStreet, newCountry)
        time.sleep(1)
        assert mpp.showTheGreenBannerForUpdatedInformation() == "Your profile is successfully updated!"
        time.sleep(2)


