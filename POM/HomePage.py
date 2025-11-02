import time

from selenium.common import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class HomePageLocators:
    linkHome = (By.XPATH, "//a[contains(text(),'Home')]")
    linkCategories = (By.XPATH, "//a[contains(text(),'Categories')]")
    linkContact = (By.XPATH, "//a[contains(text(),'Contact')]")
    linkSignIn = (By.XPATH, "//a[contains(text(),'Sign in')]")
    linkLanguages = (By.ID, "language")
    baseItemsProducts = (By.CSS_SELECTOR, "h5.card-title")
    priceForItemsProducts = (By.CSS_SELECTOR, "div.card-footer>span>span")
    itemsByCategory = (By.CSS_SELECTOR, "#filters>fieldset:nth-child(13)>div>label")
    checkBoxsCategory = (By.CSS_SELECTOR, "#filters > fieldset:nth-child(13) fieldset > div > label > input")
    searchBox = (By.ID, "search-query")
    btnSearchProduct = (By.CSS_SELECTOR, "button[data-test='search-submit']")
    sliderMinPriceLbl = (By.CSS_SELECTOR, "span.ngx-slider-pointer-min")
    sliderMaxPriceLbl = (By.CSS_SELECTOR, "span.ngx-slider-pointer-max")
    minValueOnSlider = (By.CSS_SELECTOR, "span.ngx-slider-floor")
    maxValueOnSlider = (By.CSS_SELECTOR, "span.ngx - slider - ceil")
    minPriceOverSlider = (By.CSS_SELECTOR, "Span.ngx-slider-model-value")
    maxPriceOverSlider = (By.CSS_SELECTOR, "Span.ngx-slider-bubble.ngx-slider-model-high")
    resultMsgTitle = (By.CSS_SELECTOR, "h3[data-test='search-caption']")
    resultMsgSubtitle = (By.CSS_SELECTOR, "div[data-test='no-results']")
    paginationComponent = By.CSS_SELECTOR, "a[aria-label*='Page']"
    footerCardItems = (By.CSS_SELECTOR, "div.card-footer")
    itemPrices = (By.CSS_SELECTOR, "span[data-test='product-price']")
    sortDropdown = (By.CSS_SELECTOR, "select[data-test='sort']")
    combinationPliersCard = (By.CSS_SELECTOR, "img[alt='Combination Pliers']")
    ecoLabelForAllProducts = (By.CSS_SELECTOR, "span[data-test='eco-badge']")



class HomePage:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

    def selectLinkWebInputs(self):
        self.driver.find_element(*HomePageLocators.linkSignIn).click()

    def showMeNumberProductsItemsFromHome(self):
        itemsProduct = self.driver.find_elements(*HomePageLocators.baseItemsProducts)
        for item in itemsProduct:
            print(item.text)
            # next_itemPrice = item.find_element(By.XPATH, "following-sibling::div[@class='card-footer']")
            # print(next_itemPrice.text)
        return len(itemsProduct)

    def giveMeTotalPriceFromProductsItemsFromHome(self):
        pricesProduct = self.driver.find_elements(*HomePageLocators.priceForItemsProducts)
        total = 0.0
        for price in pricesProduct:
            #print(price.text)
            price_text = price.text
            # Usamos una expresión regular para eliminar cualquier cosa que no sea un número o un punto decimal
            cleaned_price = re.sub(r'[^\d.]', '', price_text)  # Elimina el símbolo de Euro y cualquier otro carácter
            # Convertimos el precio a float
            price_value = float(cleaned_price)
            # Sumamos el precio al total
            total = round(total+price_value, 2)
        return total

    def selectedAllItemsByCategory(self):
        items = self.driver.find_elements(*HomePageLocators.itemsByCategory)
        for item in items:
            #print(item.text)
            item.click()

    def verifyIfAllItemsByCategoryAreChecked(self):
        items = self.driver.find_elements(*HomePageLocators.checkBoxsCategory)
        resultItems = []
        #esta de abajo es otra forma de recorrer una lista y ejecutar una acción sobre cada elemento
        #return [item.is_selected() for item in items]
        for item in items:
            resultItems.append(item.is_selected())
        return resultItems

    def doASearchProduct(self, productName):
        self.driver.find_element(*HomePageLocators.searchBox).send_keys(productName)
        self.driver.find_element(*HomePageLocators.btnSearchProduct).click()


    def doMoveFromMinAndMaxSlider(self, minValue, maxValue):
        action = ActionChains(self.driver)
        action.click_and_hold(self.driver.find_element(*HomePageLocators.sliderMinPriceLbl)).move_by_offset(minValue, 0).release().perform()
        action.click_and_hold(self.driver.find_element(*HomePageLocators.sliderMaxPriceLbl)).move_by_offset(maxValue, 0).release().perform()


    def verifyMinAndMaxPriceOverSlider(self):
        minPrice = self.driver.find_element(*HomePageLocators.minPriceOverSlider).text
        maxPrice = self.driver.find_element(*HomePageLocators.maxPriceOverSlider).text
        results = [minPrice, maxPrice]
        return results


    def showMeMinPriceStatus(self):
        minPriceLbl = self.driver.find_element(*HomePageLocators.minValueOnSlider).text
        maxPriceLbl = self.driver.find_element(*HomePageLocators.maxPriceOverSlider).text
        prices = [minPriceLbl, maxPriceLbl]
        return prices


    def showMeResultTitle(self):
        return self.driver.find_element(*HomePageLocators.resultMsgTitle).text


    def showMeResultSubTitle(self):
        return self.driver.find_element(*HomePageLocators.resultMsgSubtitle).text

    def showMeEachElementFromPaginationComponent(self, productName):
        page_number = 1
        while True:
            # Obtener los productos de la página actual
            names = self.driver.find_elements(*HomePageLocators.baseItemsProducts)
            # Verificar si el producto está en la página actual
            for name in names:
                if name.text.strip() == productName:
                    print(f"Producto encontrado: {name.text} en la página {page_number}")
                    return True  # Producto encontrado, devolver True

            # Si no encontramos el producto, verificar si es la última página
            if page_number == 5:  # Suponemos que hay 5 páginas en total
                print(f"Producto no encontrado en ninguna página después de recorrer la tabla.")
                break  # Salir si hemos llegado a la última página sin encontrar el producto

            # Si no encontramos el producto y no hemos llegado a la última página, ir a la siguiente página
            try:
                # Buscar el botón de la siguiente página
                page_number = page_number + 1  # Incrementamos el número de página
                self.driver.find_element(By.CSS_SELECTOR, "a[aria-label='Page-" + str(page_number) + "']").click()
                time.sleep(2)
                print(f"Cambiando a la página {page_number}")

            except IndexError:
                print("No hay más páginas. Producto no encontrado.")
                break  # Si no hay más botones de paginación, terminamos

                # Si hemos recorrido todas las páginas y no hemos encontrado el producto
        return False


    def showMeEachElementIfExistOutOfStockProduct(self, max_pages=5, retry_count=3):
        #footersCard = self.driver.find_elements(*HomePageLocators.footerCardItems)
        #names = self.driver.find_elements(*HomePageLocators.baseItemsProducts)
        # page_number = 1
        # productsItems = []
        # while page_number <= 5:
        #     footersCard = self.driver.find_elements(*HomePageLocators.footerCardItems)
        #     names = self.driver.find_elements(*HomePageLocators.baseItemsProducts)
        #
        #     for footer, name in zip(footersCard, names):
        #         if "Out of stock" in footer.text:
        #             #print("El producto con el label de Out of stock es "+name.text)
        #             #print("Y es "+footer.text)
        #             productsItems.append(name.text)
        #             productsItems.append(footer.text)
        #             return productsItems
        #
        #     # Si ya estamos en la última página, terminamos el recorrido
        #     if page_number == 5:
        #         if productsItems:
        #             return productsItems  # Si se encontraron productos, los devolvemos
        #         else:
        #             print("Producto no encontrado en ninguna página después de recorrer la tabla.")
        #             break  # Salir si hemos llegado a la última página sin encontrar el producto
        #
        #     # Ir a la siguiente página si no hemos llegado a la última
        #     try:
        #         # Buscar el botón de la siguiente página
        #         page_number = page_number + 1  # Incrementamos el número de página
        #         self.driver.find_element(By.CSS_SELECTOR, "a[aria-label='Page-" + str(page_number) + "']").click()
        #         time.sleep(2)
        #         print(f"Cambiando a la página {page_number}")
        #
        #     except IndexError:
        #          print("No hay más páginas disponibles o algo salió mal.")
        #          break  # Si no hay más botones de paginación, terminamos
        # return productsItems if productsItems else False



        products_out_of_stock = []
        page_number = 1

        while page_number <= max_pages:
            print(f"\n📄 Analizando página {page_number}...")

            try:
                # Esperar que se carguen los productos de la página actual
                self.wait.until(EC.presence_of_all_elements_located(HomePageLocators.baseItemsProducts))
                self.wait.until(EC.presence_of_all_elements_located(HomePageLocators.footerCardItems))

                total_items = len(self.driver.find_elements(*HomePageLocators.baseItemsProducts))

                for i in range(total_items):
                    for attempt in range(retry_count):
                        try:
                            # Vuelve a ubicar los elementos en cada intento
                            name_el = self.driver.find_elements(*HomePageLocators.baseItemsProducts)[i]
                            footer_el = self.driver.find_elements(*HomePageLocators.footerCardItems)[i]

                            product_name = name_el.text.strip()
                            footer_text = footer_el.text.strip()

                            if "Out of stock" in footer_text:
                                print(f"❌ Producto fuera de stock encontrado: {product_name} (página {page_number})")
                                products_out_of_stock.append({
                                    "nombre": product_name,
                                    "estado": footer_text,
                                    "pagina": page_number
                                })
                            break  # si todo fue bien, salimos del bucle interno

                        except StaleElementReferenceException:
                            if attempt < retry_count - 1:
                                time.sleep(0.3)
                                continue  # reintenta localizar el elemento
                            else:
                                print(f"⚠️ Elemento {i} dio stale tras {retry_count} intentos, continuando...")
                        except Exception as inner_e:
                            print(f"⚠️ Error inesperado en elemento {i}: {type(inner_e).__name__}")
                            break  # no reintentamos si es otro tipo de error

                # Intentar pasar a la siguiente página
                if page_number < max_pages:
                    try:
                        next_page = self.wait.until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, f"a[aria-label='Page-{page_number + 1}']"))
                        )
                        next_page.click()
                        page_number += 1

                        # Esperar a que se actualice la página
                        self.wait.until(EC.staleness_of(name_el))
                        self.wait.until(EC.presence_of_all_elements_located(HomePageLocators.baseItemsProducts))

                    except TimeoutException:
                        print(f"⚠️ No se encontró botón para página {page_number + 1}")
                        break
                else:
                    break

            except Exception as e:
                print(f"⚠️ Error general en la página {page_number}: {type(e).__name__} - {e}")
                break

        if not products_out_of_stock:
            print("✅ No se encontraron productos 'Out of stock' en ninguna página.")

        return products_out_of_stock


    def giveMeTotalPriceFromEachProductFromFivePages(self):
        page_number = 1
        totPrices = 0.0
        while page_number <= 5:
            time.sleep(1)
            #para que pueda recorrer las 5 paginas, a la lista de itemsPrices la tengo
            #que poner dentro del wile, para que en cada vuelta tome toda la lista y
            #pueda interactuar
            itemsPrices = self.driver.find_elements(*HomePageLocators.itemPrices)
            for itemPrice in itemsPrices:
                actualPrice = itemPrice.text.replace('$', '').strip()
                print(actualPrice)

                # Convertir el precio a float y sumarlo al total
                try:
                    actualPrice = float(actualPrice)
                    totPrices += actualPrice
                except ValueError:
                    print(f"Error al convertir el precio: {itemPrice.text}")

                # Si estamos en la última página, devolvemos el total acumulado
            if page_number == 5:
                return round(totPrices, 2)  # Redondear el total a 2 decimales

                # Si no estamos en la última página, avanzamos a la siguiente página
            try:
                # Buscar el botón de la siguiente página
                page_number += 1
                next_page_button = self.driver.find_element(By.CSS_SELECTOR, f"a[aria-label='Page-" + str(page_number) + "']")
                time.sleep(1)
                next_page_button.click()
                print(f"Cambiando a la página {page_number}")

            except Exception as e:
                print(f"Error al cambiar de página: {str(e)}")
                break  # Si no hay más páginas o algo sale mal, salimos del bucle

            # Si no encontramos ningún precio, devolvemos un mensaje
        print("No se pudo calcular el total. Asegúrate de que los precios están disponibles.")
        return 0.0

    def giveMeTheMostExpensiveProductFromTable(self):
        page_number = 1
        maxPrice = 0.0
        actualName = ""
        while page_number <= 5:
            time.sleep(2)
            names = self.driver.find_elements(*HomePageLocators.baseItemsProducts)
            itemsPrices = self.driver.find_elements(*HomePageLocators.itemPrices)
            for itemPrice, name in zip(itemsPrices, names):
            #for itemPrice in itemsPrices:
                actualPrice = itemPrice.text.replace('$', '').strip()
                lastActualPrice = float(actualPrice)
                #print(lastActualPrice)
                if lastActualPrice > maxPrice:
                    maxPrice = lastActualPrice
                    actualName = name.text
                    #print(maxPrice)

                # Si estamos en la última página, devolvemos el total acumulado
            if page_number == 5:
                return maxPrice, actualName  # Redondear el total a 2 decimales

                # Si no estamos en la última página, avanzamos a la siguiente página
            try:
                # Buscar el botón de la siguiente página
                page_number += 1
                next_page_button = self.driver.find_element(By.CSS_SELECTOR, f"a[aria-label='Page-" + str(page_number) + "']")
                #time.sleep(2)
                next_page_button.click()
                time.sleep(2)
                #print(f"Cambiando a la página {page_number}")

            except Exception as e:
                print(f"Error al cambiar de página: {str(e)}")
                break  # Si no hay más páginas o algo sale mal, salimos del bucle

            # Si no encontramos ningún precio, devolvemos un mensaje
        return maxPrice, actualName

    def giveMeTheMostCheapestProductFromTable(self):
        page_number = 1
        minPrice = 0.0
        actualName = ""
        firstValue = 0
        while page_number <= 5:
            time.sleep(2)
            names = self.driver.find_elements(*HomePageLocators.baseItemsProducts)
            itemsPrices = self.driver.find_elements(*HomePageLocators.itemPrices)
            for itemPrice, name in zip(itemsPrices, names):
            #for itemPrice in itemsPrices:
                actualPrice = itemPrice.text.replace('$', '').strip()
                lastActualPrice = float(actualPrice)
                #print(lastActualPrice)
                if firstValue == 0:
                    minPrice = lastActualPrice
                    firstValue = 1

                if minPrice >= lastActualPrice:
                    minPrice = lastActualPrice
                    actualName = name.text

                # Si estamos en la última página, devolvemos el total acumulado
            if page_number == 5:
                return minPrice, actualName  # Redondear el total a 2 decimales

                # Si no estamos en la última página, avanzamos a la siguiente página
            try:
                # Buscar el botón de la siguiente página
                page_number += 1
                next_page_button = self.driver.find_element(By.CSS_SELECTOR, f"a[aria-label='Page-" + str(page_number) + "']")
                #time.sleep(2)
                next_page_button.click()
                time.sleep(2)
                #print(f"Cambiando a la página {page_number}")

            except Exception as e:
                print(f"Error al cambiar de página: {str(e)}")
                break  # Si no hay más páginas o algo sale mal, salimos del bucle

            # Si no encontramos ningún precio, devolvemos un mensaje
        return minPrice, actualName


    def selectAParticularElementFromPaginationComponent(self, productName):
        page_number = 1
        while True:
            # Obtener los productos de la página actual
            names = self.driver.find_elements(*HomePageLocators.baseItemsProducts)
            # Verificar si el producto está en la página actual
            for name in names:
                if name.text.strip() == productName:
                    print(f"Producto buscado es : {name.text} y está en la página {page_number}")
                    #return True  # Producto encontrado, devolver True
                    name.click()
                    return False

            # Si no encontramos el producto, verificar si es la última página
            if page_number == 5:  # Suponemos que hay 5 páginas en total
                print(f"Producto no encontrado en ninguna página después de recorrer la tabla.")
                break  # Salir si hemos llegado a la última página sin encontrar el producto

            # Si no encontramos el producto y no hemos llegado a la última página, ir a la siguiente página
            try:
                # Buscar el botón de la siguiente página
                page_number = page_number + 1  # Incrementamos el número de página
                self.driver.find_element(By.CSS_SELECTOR, "a[aria-label='Page-" + str(page_number) + "']").click()
                time.sleep(2)
                print(f"Cambiando a la página {page_number}")

            except IndexError:
                print("No hay más páginas. Producto no encontrado.")
                break  # Si no hay más botones de paginación, terminamos
                # Si hemos recorrido todas las páginas y no hemos encontrado el producto
        return False


    def selectFilterToSortProducts(self, value):
        sortFilter = Select(self.driver.find_element(*HomePageLocators.sortDropdown))
        sortFilter.select_by_visible_text(value)


    def selectOneProductFromCard(self):
        self.driver.find_element(*HomePageLocators.combinationPliersCard).click()


    def showMeEachElementIfExistEcoLabel(self, max_pages=5):
        page_number = 1
        all_product_names = []

        while page_number <= max_pages:
            try:
                # Esperar a que se carguen los productos en la página
                self.wait.until(EC.presence_of_all_elements_located(HomePageLocators.baseItemsProducts))
                product_containers = self.driver.find_elements(*HomePageLocators.baseItemsProducts)

                print(f"\nPágina {page_number}:")
                for container in product_containers:
                    try:
                        product_name = container.text.strip()
                        print(f"- {product_name}")
                        all_product_names.append(product_name)
                    except:
                        # Si no se encuentra el nombre del producto, mostrar contenedor completo (fallback)
                        print(f"- [NO SE PUDO EXTRAER NOMBRE]: {container.text.strip()}")

                # Ir a la siguiente página si corresponde
                page_number += 1
                if page_number <= max_pages:
                    try:
                        next_page_button = self.wait.until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, f"a[aria-label='Page-{page_number}']"))
                        )
                        next_page_button.click()
                    except TimeoutException:
                        print(f"No se encontró el botón para la página {page_number}")
                        break
            except TimeoutException:
                print("No se pudieron cargar los productos de la página.")
                break

        return all_product_names



