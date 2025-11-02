from selenium.webdriver.common.by import By


class RentalsPageLocators:
    listItems = (By.CSS_SELECTOR, "div.row.no-gutters")
    titleItems = (By.CSS_SELECTOR, "h5.card-title")
    descriptionItems = (By.CSS_SELECTOR, "p.card-text")


class RentalsPage:

    def __init__(self, driver):
        self.driver = driver

    def showTheListOfWantedProducts(self):
        itmesTitle = self.driver.find_elements(*RentalsPageLocators.titleItems)
        itmesDescription = self.driver.find_elements(*RentalsPageLocators.descriptionItems)
        itemsName = []
        for title, description in zip(itmesTitle, itmesDescription):
            itemsName.append(title.text)
        return itemsName

    def showMeTheDescriptionForAParticularProduct(self, searchItem):
        itmesTitle = self.driver.find_elements(*RentalsPageLocators.titleItems)
        itmesDescription = self.driver.find_elements(*RentalsPageLocators.descriptionItems)
        for title, description in zip(itmesTitle, itmesDescription):
            if title.text == searchItem:
                return description.text
        return "No se ha encontrado el producto buscado"