import json
import time

from POM.HeaderMenuPage import HeaderMenuPage
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage
from POM.MyAccountPage import MyAccountPage
from POM.MyFavoritePage import MyFavoritePage
from POM.ProductDetailPage import ProductDetailPage
from Utils.BaseClass import BaseClass


class TestBeingLoggedVerifyThatICanAddAFavoriteProduct(BaseClass):

      def test_BeingLoggedVerifyThatICanAddAFavoriteProduct(self):
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
        hmp.selectAParticularCategory("My favorites")
        time.sleep(1)
        mfp.deleteAllItemsFromMyFavoritesPage()
        time.sleep(1)
        hmp.selectLogoToRedirectHomePage()
        hp = HomePage(driver)
        time.sleep(1)
        productName = "Combination Pliers"
        hp.selectAParticularElementFromPaginationComponent(productName)
        pdp = ProductDetailPage(driver)
        time.sleep(1)
        pdp.addAsFavoriteProduct()
        time.sleep(3)
        assert pdp.verifyIfAddMyFavoriteListProductIsPresented() == "Product added to your favorites list."
        time.sleep(1)
        hmp.selectLogoToRedirectHomePage()
        time.sleep(1)
        hmp.selectMyAccountNameOption()
        time.sleep(3)
        hmp.selectAParticularCategory("My favorites")
        mfp.deleteAllItemsFromMyFavoritesPage()
        time.sleep(2)
        assert "There are no favorites yet." in mfp.verifyThatFavoriteProductListIsEmpty()
        time.sleep(3)


