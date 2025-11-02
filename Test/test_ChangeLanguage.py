import json
import time

from POM.HeaderMenuPage import HeaderMenuPage
from Utils.BaseClass import BaseClass


class TestChangeLanguage(BaseClass):

      def test_ChangeLanguage(self):
        log = self.get_Logger()
        log.info("Change Language test")
        driver = self.driver
        itemsExpectedSpanish = ['Inicio', 'Contacto', 'Iniciar sesión']
        hmp = HeaderMenuPage(driver)
        hmp.selectLinkLanguages()
        time.sleep(1)
        hmp.changeEsLanguageFromDropdownLanguages()
        time.sleep(1)
        itemsActualSpanish = hmp.verifyIfLanguageWasChangedToSpanish()
        time.sleep(1)
        assert itemsActualSpanish == itemsExpectedSpanish
        time.sleep(3)
