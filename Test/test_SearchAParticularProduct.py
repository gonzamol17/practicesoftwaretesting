import json
import time

from selenium.webdriver.common.by import By

from POM.HeaderMenuPage import HeaderMenuPage
from POM.HomePage import HomePage
from POM.ResultPage import ResultPage
from Utils.BaseClass import BaseClass


class TestSearchAParticular_Product(BaseClass):

      def test_SearchAParticular_Product(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        hp = HomePage(driver)
        productName = "Hammer"
        hp.doASearchProduct(productName)
        time.sleep(3)
        rp = ResultPage(driver)
        itemsSearched = rp.showTheListOfWantedProducts()
        # for item in itemsSearched:
        #     print(item)
        #     assert productName in item
        #la linea de abajo reempla al ciclo for para hacer un assert en cada elemento del array verificando
        #que en cada resultado exista el producto que se está buscando
        assert all(productName.lower() in item.lower() for item in itemsSearched)



