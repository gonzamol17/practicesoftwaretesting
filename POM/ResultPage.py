from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    txtFirstName = (By.ID, "first_name")
    titleProducts = (By.CSS_SELECTOR, "h5[class='card-title']")
    priceProducts = (By.CSS_SELECTOR, "span[data-test='product-price']")


class ResultPage:

    def __init__(self, driver):
        self.driver = driver

    def showTheListOfWantedProducts(self):
        n = 1
        totItems = len(self.driver.find_elements(*RegistrationPageLocators.titleProducts))
        itmes = self.driver.find_elements(*RegistrationPageLocators.titleProducts)
        print("En total se están visualizando la cantidad de :"+str(totItems)+" items")
        itemPro = []
        for item in itmes:
            print("El producto nro "+str(n)+" es "+item.text)
            itemPro.append(item.text)
            n = n+1
        return itemPro


    def showThePricesForWantedProducts(self):
        n = 1
        itmes = self.driver.find_elements(*RegistrationPageLocators.priceProducts)
        pricesPro = []
        for item in itmes:
            #print("El precio nro "+str(n)+" es "+item.text)
            price_text = item.text.replace('$', '').strip()  # Eliminar el símbolo y los espacios adicionales
            #price = float(price_text)
            #print("El precio editado sin el símbolo $ es: "+price_text)
            pricesPro.append(float(price_text))
            n = n+1
        total_price = sum(pricesPro)
        return total_price

    def showTheItemsForPricesMoreThanAValue(self, value):
        itmesPrice = self.driver.find_elements(*RegistrationPageLocators.priceProducts)
        itmesName = self.driver.find_elements(*RegistrationPageLocators.titleProducts)
        pricesList = []
        # Recorreremos los precios y nombres de los productos, este tipo de for me permite recorrer dos listas con el
        #mismo tamaño para cuando encuentro un elemento en una de las listas, pueda mostrar el valor de otro elemento en la otra lista
        for price, name in zip(itmesPrice, itmesName):
            price_text = price.text.strip().replace('$', '').replace(',', '')  # Eliminamos el símbolo y comas si es necesario
            try:
                price_value = float(price_text)  # Convertimos el texto a float
            except ValueError:
                price_value = 0.0  # Si el valor no se puede convertir, asignamos 0.0
            # Si el precio es mayor que el valor proporcionado, lo añadimos a la lista
            if price_value > value:
                # Mostramos nombre y precio del producto
                pricesList.append((name.text, price_value))
                print(f"Producto: {name.text}, Precio: ${price_value}")
        return pricesList
