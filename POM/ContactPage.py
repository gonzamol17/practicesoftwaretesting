from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ContactPageLocators:
    subjectDropdown = (By.ID, "subject")
    txtBoxMessage = (By.ID, "message")
    btnSubmitMsg = (By.CSS_SELECTOR, "input[class ='btnSubmit']")
    greenMsgConfirmed = (By.CSS_SELECTOR, "div[class='alert alert-success mt-3']")



class ContactPage:

    def __init__(self, driver):
        self.driver = driver

    def completeTheFormContact(self, subject, msg):
        dropdown = self.driver.find_element(*ContactPageLocators.subjectDropdown)
        option = Select(dropdown)
        option.select_by_visible_text(subject)
        self.driver.find_element(*ContactPageLocators.txtBoxMessage).send_keys(msg)
        self.driver.find_element(*ContactPageLocators.btnSubmitMsg).click()

    def showConfirmMsg(self):
        return self.driver.find_element(*ContactPageLocators.greenMsgConfirmed).text

