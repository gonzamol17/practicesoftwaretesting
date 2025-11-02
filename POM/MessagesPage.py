from selenium.webdriver.common.by import By


class MessagePageLocators:
    subject = (By.CSS_SELECTOR, "tbody tr td:nth-child(1)")
    msg = (By.CSS_SELECTOR, "tbody tr td:nth-child(2)")
    status = (By.CSS_SELECTOR, "tbody tr td:nth-child(3)")
    btnMoreDetails = (By.CSS_SELECTOR, "a.btn.btn-sm:nth-of-type(1)")
    detailsOfMsg = (By.CSS_SELECTOR, "p.card-text")



class MessagePage:

    def __init__(self, driver):
        self.driver = driver

    def showMeSubject(self):
        return self.driver.find_element(*MessagePageLocators.subject).text.capitalize()

    def showMeMsg(self):
        return self.driver.find_element(*MessagePageLocators.msg).text

    def showMeStatus(self):
        return self.driver.find_element(*MessagePageLocators.status).text

    def selectBtnMoreDetails(self):
        self.driver.find_element(*MessagePageLocators.btnMoreDetails).click()

    def getDetailsOfMsg(self):
        return self.driver.find_element(*MessagePageLocators.detailsOfMsg).text

