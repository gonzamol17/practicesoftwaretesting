from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    txtFirstName = (By.ID, "first_name")
    txtLastName = (By.ID, "last_name")
    txtDayOfBirth = (By.ID, "dob")
    txtAddress = (By.ID, "street")
    txtPostCode = (By.ID, "postal_code")
    txtCity = (By.ID, "city")
    txtState = (By.ID, "state")
    txtCountry = (By.ID, "country")
    txtPhone = (By.ID, "phone")
    txtEmail = (By.ID, "email")
    txtPassword = (By.ID, "password")
    btnRegister = (By.CSS_SELECTOR, "button.btnSubmit")


class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver

    def completeRegisterForm(self, txtFirstName, txtLastName, txtDayOfBirth, txtAddress, txtPostCode, txtCity, txtState, txtCountry, txtPhone, txtEmail, txtPassword):
        self.driver.find_element(*RegistrationPageLocators.txtFirstName).send_keys(txtFirstName)
        self.driver.find_element(*RegistrationPageLocators.txtLastName).send_keys(txtLastName)
        self.driver.find_element(*RegistrationPageLocators.txtDayOfBirth).send_keys(txtDayOfBirth)
        self.driver.find_element(*RegistrationPageLocators.txtAddress).send_keys(txtAddress)
        self.driver.find_element(*RegistrationPageLocators.txtPostCode).send_keys(txtPostCode)
        self.driver.find_element(*RegistrationPageLocators.txtCity).send_keys(txtCity)
        self.driver.find_element(*RegistrationPageLocators.txtState).send_keys(txtState)
        self.driver.find_element(*RegistrationPageLocators.txtCountry).send_keys(txtCountry)
        self.driver.find_element(*RegistrationPageLocators.txtPhone).send_keys(txtPhone)
        self.driver.find_element(*RegistrationPageLocators.txtEmail).send_keys(txtEmail)
        self.driver.find_element(*RegistrationPageLocators.txtPassword).send_keys(txtPassword)
        self.driver.find_element(*RegistrationPageLocators.btnRegister).click()













