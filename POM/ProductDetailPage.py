import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By


class ProductDetailPageLocators:
    productTitle = (By.CSS_SELECTOR, "h1[data-test='product-name']")
    btn_AddFavorites = (By.ID, "btn-add-to-favorites")
    redBannerMsgNoAddFavorites = (By.CSS_SELECTOR, ".toast-message.ng-star-inserted")
    redBannerColorNoAddFavorites = (By.CSS_SELECTOR, "div.ngx-toastr.toast-error")
    btn_QuantityIncrease = (By.ID, "btn-increase-quantity")
    btn_AddToCart = (By.ID, "btn-add-to-cart")
    greenBannerAddToCart = (By.ID, "toast-container")
    iconCartQuantity = (By.ID, "lblCartCount")
    relatedProductsTitle = (By.XPATH, "//h2[normalize-space()='Related products']")
    listOfRelatedProductsTitles = (By.CSS_SELECTOR, "h5.card-title")
    greenBannerAddMyFavoriteList = (By.CSS_SELECTOR, "div.ng-tns-c969959638-0.toast-message.ng-star-inserted")
    priceProduct = (By.CSS_SELECTOR, "span[data-test='unit-price']")



class ProductDetailPage:

    def __init__(self, driver):
        self.driver = driver

    def showTheProductTitle(self):
        return self.driver.find_element(*ProductDetailPageLocators.productTitle).text

    def addAsFavoriteProduct(self):
        self.driver.find_element(*ProductDetailPageLocators.btn_AddFavorites).click()

    def verifyIfRedBannerForNoAddFavoriteProductIsPresented(self):
        return self.driver.find_element(*ProductDetailPageLocators.redBannerMsgNoAddFavorites).is_displayed()

    def showMeTextAndColorFromRedBanner(self):
        return (self.driver.find_element(*ProductDetailPageLocators.redBannerMsgNoAddFavorites).text, self.driver.find_element(*ProductDetailPageLocators.redBannerColorNoAddFavorites).value_of_css_property("background-color"))

    def increaseQuantityProduct(self, quantity):
        for i in range(1, quantity):
            self.driver.find_element(*ProductDetailPageLocators.btn_QuantityIncrease).click()
        self.driver.find_element(*ProductDetailPageLocators.btn_AddToCart).click()

    def verifyTheGreenBannerIsPresented(self):
        return self.driver.find_element(*ProductDetailPageLocators.redBannerMsgNoAddFavorites).text

    def verifyTheQuantityFromCartIcon(self):
        return self.driver.find_element(*ProductDetailPageLocators.iconCartQuantity).text

    def selectTheAddToCartBtn(self):
        self.driver.find_element(*ProductDetailPageLocators.btn_AddToCart).click()
        time.sleep(1)
        self.driver.find_element(*ProductDetailPageLocators.greenBannerAddToCart).click()

    def verifyIfRelatedProductTitleIsPresented(self):
        return self.driver.find_element(*ProductDetailPageLocators.relatedProductsTitle).text

    def checkTheNumberOfRelatedProducts(self):
        titles = self.driver.find_elements(*ProductDetailPageLocators.listOfRelatedProductsTitles)
        n = 1
        for title in titles:
            print(f'El producto número {n} dentro de Related Products: {title.text}')
            n = n+1
        return len(self.driver.find_elements(*ProductDetailPageLocators.listOfRelatedProductsTitles))

    def verifyIfAddMyFavoriteListProductIsPresented(self):
        return self.driver.find_element(*ProductDetailPageLocators.greenBannerAddMyFavoriteList).text

    def getIndividualProductPrice(self):
        return self.driver.find_element(*ProductDetailPageLocators.priceProduct).text
