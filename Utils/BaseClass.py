import inspect
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


#ver si en esta clase base esta anotación de pytest.mark va también, porque ya la estamos usando en la clase
# que contiene el test. Por lo tanto dentro de la clase del Test, lo único que hay que hacer es llamar
# a esta clase base, para que pueda usar estos métodos heredados
@pytest.mark.usefixtures("test_setup")
class BaseClass:

    def get_Logger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        fileHandler = logging.FileHandler("..\\Data\\logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger
