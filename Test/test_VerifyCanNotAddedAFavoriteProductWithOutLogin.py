import time
from POM.HomePage import HomePage
from POM.ProductDetailPage import ProductDetailPage
from Utils.BaseClass import BaseClass


class TestVerifyCanNotAddedAFavoriteProductWithOutLogin(BaseClass):

      def test_VerifyCanNotAddedAFavoriteProductWithOutLogin(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        hp = HomePage(driver)
        productName = "Belt Sander"
        hp.selectAParticularElementFromPaginationComponent(productName)
        pdp = ProductDetailPage(driver)
        pdp.addAsFavoriteProduct()
        assert pdp.verifyIfRedBannerForNoAddFavoriteProductIsPresented()
        assert pdp.showMeTextAndColorFromRedBanner()[0] == "Unauthorized, can not add product to your favorite list." and pdp.showMeTextAndColorFromRedBanner()[1] == "rgba(189, 54, 47, 1)"
        time.sleep(2)


