import json
import time

from POM.HomePage import HomePage
from Utils.BaseClass import BaseClass


class TestVerifyHandsToolsCheckbox(BaseClass):

      def test_VerifyHandsToolsCheckbox(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        hp = HomePage(driver)
        driver.execute_script("window.scrollTo(0, 800)")
        time.sleep(2)
        hp.selectedAllItemsByCategory()
        time.sleep(5)
        items = hp.verifyIfAllItemsByCategoryAreChecked()
        #En este caso la función all(items) lo que hace es iterar sobre cada elemento del array y devolver un solo
        #true si todos los elementos son True, o false si hay al menos un elemento False y luego hago el asser con True
        #assert all(items) is True
        #En el caso de arriba no hace falta poner "is True", porque ya la función all(items) devuelve true o false
        assert all(items)
        time.sleep(2)
