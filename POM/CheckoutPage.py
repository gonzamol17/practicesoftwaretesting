import re
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CheckoutPageLocators:
    btn_Remove = (By.CSS_SELECTOR, "a.btn.btn-danger")
    emptyShoppingCartMsg = (By.XPATH, "//p[normalize-space()='The cart is empty. Nothing to display.']")
    itemPrice = (By.XPATH, "//span[@data-test='product-price']")
    btnCheckout = (By.CSS_SELECTOR, "div[class='ng-star-inserted'] button[type='button']")
    firstCircleBar = (By.CSS_SELECTOR, "li[class='ng-star-inserted done navigable'] div:nth-child(2)")
    msgSuccessOnSecondStep = (By.CSS_SELECTOR, "p[class='ng-star-inserted']")
    btnTwoCheckout = (By.CSS_SELECTOR, "button[data-test='proceed-1']")
    secondCircleBar = (By.CSS_SELECTOR, "li:nth-child(2)>a>div.step-indicator")
    btnThreeCheckout = (By.CSS_SELECTOR, "button[data-test='proceed-2']")
    btnForthCheckout = (By.CSS_SELECTOR, "button[data-test='proceed-3']")
    thirdCircleBar = (By.CSS_SELECTOR, "li:nth-child(3)>a>div.step-indicator")
    fourthCircleBar = (By.CSS_SELECTOR, "li:nth-child(4)>a>div.step-indicator")
    paymentMethodDropdown = (By.ID, "payment-method")
    creditCardField = (By.ID, "credit_card_number")
    expirationDateField = (By.ID, "expiration_date")
    cvvField = (By.ID, "cvv")
    cardHoldNameField = (By.ID, "card_holder_name")
    btnSubmit = (By.CSS_SELECTOR, "button[data-test='finish']")
    greenBannerPaymentConfirmed = (By.CSS_SELECTOR, "div[data-test='payment-success-message']")
    lastBtnConfirm = (By.CSS_SELECTOR, "button[data-test='finish']")
    msgConfirmationPayment = (By.ID, "order-confirmation")


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    def cleanShoppingCart(self):
        buttons = self.driver.find_elements(*CheckoutPageLocators.btn_Remove)
        for button in buttons:
            button.click()

    def getIndividualProductPriceFromCheckout(self):
        return self.driver.find_element(*CheckoutPageLocators.itemPrice).text

    def selectTheCheckoutBtn(self):
        self.driver.find_element(*CheckoutPageLocators.btnCheckout).click()

    def getColorFromFirstCircleBar(self):
        return self.driver.find_element(*CheckoutPageLocators.firstCircleBar).value_of_css_property("background-color")

    def getSuccessfullMsgOnSecondStep(self):
        return self.driver.find_element(*CheckoutPageLocators.msgSuccessOnSecondStep).text

    def selectTheSecondCheckoutBtn(self):
        self.driver.find_element(*CheckoutPageLocators.btnTwoCheckout).click()

    def getColorFromSecondCircleBar(self):
        return self.driver.find_element(*CheckoutPageLocators.secondCircleBar).value_of_css_property("background-color")

    def selectTheThirdCheckoutBtn(self):
        self.driver.find_element(*CheckoutPageLocators.btnThreeCheckout).click()

    def selectTheForthCheckoutBtn(self):
        self.driver.find_element(*CheckoutPageLocators.btnForthCheckout).click()

    def getColorFromThirdCircleBar(self):
        return self.driver.find_element(*CheckoutPageLocators.thirdCircleBar).value_of_css_property("background-color")

    def getColorFromFourthCircleBar(self):
        return self.driver.find_element(*CheckoutPageLocators.fourthCircleBar).value_of_css_property("background-color")

    def selectThePaymentMethodValue(self, valor):
        dropdown = self.driver.find_element(*CheckoutPageLocators.paymentMethodDropdown)
        #dropdown.click()#in this case i dont need to do click over the dropdown
        option = Select(dropdown)
        option.select_by_visible_text(valor)

    def completeActionToPayment(self, creditCardNumber, date, cvv, cardHolderName):
        self.driver.find_element(*CheckoutPageLocators.creditCardField).send_keys(creditCardNumber)
        self.driver.find_element(*CheckoutPageLocators.expirationDateField).send_keys(date)
        self.driver.find_element(*CheckoutPageLocators.cvvField).send_keys(cvv)
        self.driver.find_element(*CheckoutPageLocators.cardHoldNameField).send_keys(cardHolderName)
        self.driver.find_element(*CheckoutPageLocators.btnSubmit).click()

    def getSuccessfullMsgPaymentConfirmed(self):
        return self.driver.find_element(*CheckoutPageLocators.greenBannerPaymentConfirmed).text

    def verifyIfBtnConfirmArePresent(self):
        return self.driver.find_element(*CheckoutPageLocators.lastBtnConfirm).is_displayed()

    def selectTheLastBtnConfirm(self):
        self.driver.find_element(*CheckoutPageLocators.lastBtnConfirm).click()

    def getOrderInvoiceConfirmed(self):
        return self.driver.find_element(*CheckoutPageLocators.msgConfirmationPayment).text

    def getInvoiceNumber(self, invoiceNum):
        match = re.search(r'INV-\d+', invoiceNum)
        if match:
            return match.group()
        else:
            return None