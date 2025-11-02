import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class MyProfilePageLocators:
    txtFieldAddress = (By.ID, "street")
    txtFieldCountry = (By.ID, "country")
    btnUpdated = (By.CSS_SELECTOR, "button[data-test='update-profile-submit']")
    bannerDataUpdated = (By.CSS_SELECTOR, "[class='alert alert-success mt-3']")


class MyProfilePage:

    def __init__(self, driver):
        self.driver = driver

    def updateAddress(self, street, country):
        self.driver.find_element(*MyProfilePageLocators.txtFieldAddress).clear()
        self.driver.find_element(*MyProfilePageLocators.txtFieldAddress).send_keys(street)
        self.driver.find_element(*MyProfilePageLocators.txtFieldCountry).clear()
        time.sleep(1)
        self.driver.find_element(*MyProfilePageLocators.txtFieldCountry).send_keys(country)
        self.driver.find_element(*MyProfilePageLocators.btnUpdated).click()

    def showTheGreenBannerForUpdatedInformation(self):
        return self.driver.find_element(*MyProfilePageLocators.bannerDataUpdated).text




