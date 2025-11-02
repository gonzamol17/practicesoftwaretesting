import time

from selenium.webdriver.common.by import By


class MyFavoritePageLocators:
    itemsProductsToDelete = (By.CSS_SELECTOR, "button[data-test='delete']")
    msgWhereFavoriteItemsItsEmpty = (By.CSS_SELECTOR, "div[class='col']>div")


class MyFavoritePage:

    def __init__(self, driver):
        self.driver = driver

    def deleteAllItemsFromMyFavoritesPage(self):
        items = self.driver.find_elements(*MyFavoritePageLocators.itemsProductsToDelete)
        if not items:
            print("No hay productos en favoritos para eliminar.")
            return  # o simplemente pasa si no quieres hacer nada
        for item in items:
            item.click()

    def verifyThatFavoriteProductListIsEmpty(self):
        return self.driver.find_element(*MyFavoritePageLocators.msgWhereFavoriteItemsItsEmpty).text


