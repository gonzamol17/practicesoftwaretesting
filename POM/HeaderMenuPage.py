import time

from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HeaderMenuPageLocators:
    linkHome = (By.XPATH, "//a[contains(text(),'Home')]")
    linkCategories = (By.XPATH, "//a[contains(text(),'Categories')]")
    linkContact = (By.XPATH, "//a[contains(text(),'Contact')]")
    linkSignIn = (By.XPATH, "//a[contains(text(),'Sign in')]")
    linkLanguages = (By.ID, "language")
    dropdownLanguages = (By.CSS_SELECTOR, "#dropdown-animated>li>a")
    itemsFromHeaderMenu = (By.CSS_SELECTOR, "[class='nav-item']>a")
    itemsFromCategories = (By.CSS_SELECTOR, "ul.dropdown-menu.show a")
    shoppingCartItem = (By.CSS_SELECTOR, "a[data-test='nav-cart']")
    linkRedirectHomePage = (By.CSS_SELECTOR, "a[class='navbar-brand']")
    myAccountName = (By.ID, "menu")
    listFromMyAccountName = (By.CSS_SELECTOR, "ul.dropdown-menu.show")
    greenBannerAddToCart = (By.XPATH, "div[aria-label='Product added to shopping cart.']")
    myInvoicesOption = (By.CSS_SELECTOR, "ul[class='dropdown-menu show'] li:nth-child(4)")
    myMessagesOption = (By.CSS_SELECTOR, "ul[class='dropdown-menu show'] li:nth-child(5)")


class HeaderMenuPage:

    def __init__(self, driver):
        self.driver = driver

    def selectLinkHome(self):
        self.driver.find_element(*HeaderMenuPageLocators.linkHome).click()

    def selectLinkCategories(self):
        self.driver.find_element(*HeaderMenuPageLocators.linkCategories).click()

    def selectLinkContact(self):
        self.driver.find_element(*HeaderMenuPageLocators.linkContact).click()

    def selectLinkSignIn(self):
        self.driver.find_element(*HeaderMenuPageLocators.linkSignIn).click()

    def selectLinkLanguages(self):
        self.driver.find_element(*HeaderMenuPageLocators.linkLanguages).click()

    def changeEsLanguageFromDropdownLanguages(self):
        dropdownListItems = self.driver.find_elements(*HeaderMenuPageLocators.dropdownLanguages)
        for item in dropdownListItems:
            if item.text == "ES":
                item.click()

    def verifyIfLanguageWasChangedToSpanish(self):
        items = self.driver.find_elements(*HeaderMenuPageLocators.itemsFromHeaderMenu)
        headersItems = []
        for item in items:
            headersItems.append(item.text)
        return headersItems

    def verifyAllTheCategoriesItems(self):
        items = self.driver.find_elements(*HeaderMenuPageLocators.itemsFromCategories)
        categoriesItems = []
        for item in items:
            categoriesItems.append(item.text)
        return categoriesItems


    def selectAParticularCategory(self, category):
        items = self.driver.find_elements(*HeaderMenuPageLocators.itemsFromCategories)
        for item in items:
            if item.text == category:
                item.click()

    def selectShoppingCartItem(self):
        self.driver.find_element(*HeaderMenuPageLocators.shoppingCartItem).click()


    def verifyIfShoppingCartIsPresent(self):
        try:
            # Intentamos encontrar el elemento
            self.driver.find_element(*HeaderMenuPageLocators.shoppingCartItem)
            return True  # El elemento fue encontrado, devolvemos True
        except NoSuchElementException:
            return False  # Si el elemento no fue encontrado, devolvemos False


    def selectLogoToRedirectHomePage(self):
        self.driver.find_element(*HeaderMenuPageLocators.linkRedirectHomePage).click()

    def selectMyAccountNameOption(self):
        self.driver.find_element(*HeaderMenuPageLocators.myAccountName).click()

    def showMeListFromMyAccountName(self):
        items = self.driver.find_elements(*HeaderMenuPageLocators.listFromMyAccountName)
        list = []
        for item in items:
            list.extend(item.text.split('\n'))
        return list

    def selectMyInvoicesOption(self):
        self.driver.find_element(*HeaderMenuPageLocators.myInvoicesOption).click()

    def selectMyMessagesOption(self):
        self.driver.find_element(*HeaderMenuPageLocators.myMessagesOption).click()

    def selectContactOption(self):
        self.driver.find_element(*HeaderMenuPageLocators.linkContact).click()