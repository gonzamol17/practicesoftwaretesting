from selenium.webdriver.common.by import By


class MyAccountPageLocators:
    myAccountTitle = (By.XPATH, "//h1[contains(text(),'My account')]")
    myAccountItems = (By.CSS_SELECTOR, "a.btn.btn-outline-secondary")


class MyAccountPage:

    def __init__(self, driver):
        self.driver = driver

    def showMeMyAccountTitle(self):
        return self.driver.find_element(*MyAccountPageLocators.myAccountTitle).text

    def showMyAccountItems(self):
        items = self.driver.find_elements(*MyAccountPageLocators.myAccountItems)
        itemsList = []
        for item in items:
            #print(item.text)
            itemsList.append(item.text)
        return itemsList

