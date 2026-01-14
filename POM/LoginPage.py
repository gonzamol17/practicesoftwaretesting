from selenium.webdriver.common.by import By


class LoginPageLocators:
    txtEmail = (By.ID, "email")
    txtPassword = (By.ID, "password")
    linkRegisterAccount = (By.XPATH, "//a[contains(text(),'Registra tu cuenta')]")
    titleLogin = (By.XPATH, "//h3[contains(text(),'Iniciar sesión')]")
    btnLogin = (By.CSS_SELECTOR, "input.btnSubmit")
    validationErrorEmail = (By.ID, "email-error")
    validationErrorPass = (By.ID, "password-error")
    linkForgotPassword = (By.CSS_SELECTOR, "a.ForgetPwd")



class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def completeSignInAction(self, email, password):
        self.driver.find_element(*LoginPageLocators.txtEmail).send_keys(email)
        self.driver.find_element(*LoginPageLocators.txtPassword).send_keys(password)
        self.driver.find_element(*LoginPageLocators.btnLogin).click()

    def selectRegisterLinkOption(self):
        self.driver.find_element(*LoginPageLocators.linkRegisterAccount).click()

    def showLoginTitle(self):
        return self.driver.find_element(*LoginPageLocators.titleLogin).text

    def selectBtnLogin(self):
        self.driver.find_element(*LoginPageLocators.btnLogin).click()

    def showEmailErrorValidationLogin(self):
        return self.driver.find_element(*LoginPageLocators.validationErrorEmail).text

    def showPassErrorValidationLogin(self):
        return self.driver.find_element(*LoginPageLocators.validationErrorPass).text

    def showEmailColorErrorField(self):
        return self.driver.find_element(*LoginPageLocators.txtEmail).value_of_css_property("border-color")

    def showPassColorerrorField(self):
        return self.driver.find_element(*LoginPageLocators.txtPassword).value_of_css_property("border-color")

    def selectForgotPasswordOption(self):
        self.driver.find_element(*LoginPageLocators.linkForgotPassword).click()








