import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ForgotPasswordPageLocators:
    titleForgotPassword = (By.XPATH, "//h3[contains(text(),'Forgot Password')]")
    emailTxt = (By.ID, "email")
    setNewPassword = (By.CSS_SELECTOR, "input.btnSubmit")
    errorValidationMsg = (By.CSS_SELECTOR, "[role='alert']")


class ForgotPasswordPage:

    def __init__(self, driver):
        self.driver = driver

    def showMainTitleForgotPassword(self):
        return self.driver.find_element(*ForgotPasswordPageLocators.titleForgotPassword).text

    def doRecoverPasswordAction(self, email):
        self.driver.find_element(*ForgotPasswordPageLocators.emailTxt).send_keys(email)
        self.driver.find_element(*ForgotPasswordPageLocators.setNewPassword).click()

    def showMsgError(self):
        return self.driver.find_element(*ForgotPasswordPageLocators.errorValidationMsg).text
