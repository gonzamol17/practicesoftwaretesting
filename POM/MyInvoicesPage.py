from selenium.webdriver.common.by import By


class MyAccountPageLocators:
    invoiceNumber = (By.CSS_SELECTOR, "tbody tr td:nth-child(1)")



class MyInvoicesPage:

    def __init__(self, driver):
        self.driver = driver

    def showMeMyLastInvoice(self):
        return self.driver.find_element(*MyAccountPageLocators.invoiceNumber).text

