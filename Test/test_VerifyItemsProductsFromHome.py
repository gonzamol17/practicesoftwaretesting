import time

from POM.HomePage import HomePage
from Utils.BaseClass import BaseClass


class TestVerifyItemsProductsFromHome(BaseClass):

      def test_VerifyItemsProductsFromHome(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        hp = HomePage(driver)
        items = hp.showMeNumberProductsItemsFromHome()
        total = hp.giveMeTotalPriceFromProductsItemsFromHome()
        print("La Cantidad total de Productos listados en el home son: "+str(items))
        assert 146.59 == total
        print("El monto total de Euros de los items listados x defaul en el home es de: "+str(total))
        time.sleep(3)
