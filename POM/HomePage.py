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
    cardContainer = (By.CSS_SELECTOR, "a.card")
    co2labels = (By.CSS_SELECTOR, "span.co2-letter.active")


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

    def findProductAndGetCo2FromCard(self, product_name, max_pages=6):
        page_number = 1

        while page_number <= max_pages:
            print(f"🔍 Buscando '{product_name}' en página {page_number}")
            self.wait.until(
                EC.presence_of_all_elements_located(HomePageLocators.cardContainer)
            )

            cards = self.driver.find_elements(*HomePageLocators.cardContainer)

            for card in cards:
                try:
                    name = card.find_element(
                        *HomePageLocators.baseItemsProducts
                    ).text.strip()

                    if product_name.lower() in name.lower():
                        print(f"✅ Producto encontrado: {name}")

                        # 👇 CO2 SOLO del card correcto
                        co2_label = card.find_element(
                            *HomePageLocators.co2labels
                        ).text.strip()
                        print(f"🌱 CO2 en card: {co2_label}")
                        card.click()
                        return co2_label

                except NoSuchElementException:
                    continue
                except StaleElementReferenceException:
                    return self.findProductAndGetCo2FromCard(product_name, max_pages)

            # paginación
            if page_number < max_pages:
                next_page = self.wait.until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, f"a[aria-label='Page-{page_number + 1}']")
                    )
                )
                old_card = cards[0]
                next_page.click()
                self.wait.until(EC.staleness_of(old_card))
                page_number += 1
            else:
                break
        raise AssertionError(f"❌ Producto '{product_name}' no encontrado")



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

    def selectAParticularElementFromPaginationComponent(self, productName, max_pages=6):
        page_number = 1

        while page_number <= max_pages:
            print(f"🔍 Buscando '{productName}' en página {page_number}")

            self.wait.until(
                EC.presence_of_all_elements_located(HomePageLocators.cardContainer)
            )

            cards = self.driver.find_elements(*HomePageLocators.cardContainer)

            for card in cards:
                try:
                    name = card.find_element(*HomePageLocators.baseItemsProducts).text.strip()

                    # 👇 comparación más tolerante
                    if productName.lower() in name.lower():
                        print(f"✅ Producto encontrado: {name} en página {page_number}")
                        card.click()
                        return

                except StaleElementReferenceException:
                    return self.selectAParticularElementFromPaginationComponent(productName, max_pages)

            if page_number < max_pages:
                next_page = self.wait.until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, f"a[aria-label='Page-{page_number + 1}']")
                    )
                )

                old_card = cards[0]
                next_page.click()
                self.wait.until(EC.staleness_of(old_card))
                page_number += 1
            else:
                break

        raise AssertionError(f"❌ El producto '{productName}' no fue encontrado en ninguna página")


    def selectFilterToSortProducts(self, value):
        sortFilter = Select(self.driver.find_element(*HomePageLocators.sortDropdown))
        sortFilter.select_by_visible_text(value)


    def selectOneProductFromCard(self):
        self.driver.find_element(*HomePageLocators.combinationPliersCard).click()


    def showMeEachElementIfExistEcoLabel(self):
        eco_products = []
        page_number = 1

        while True:
            print(f"\n📄 Analizando página {page_number}...")

            self.wait.until(EC.presence_of_all_elements_located(HomePageLocators.cardContainer))
            cards = self.driver.find_elements(*HomePageLocators.cardContainer)

            first_product_name = cards[0].find_element(
                *HomePageLocators.baseItemsProducts
            ).text

            for card in cards:
                try:
                    product_name = card.find_element(
                        *HomePageLocators.baseItemsProducts
                    ).text.strip()

                    if card.find_elements(*HomePageLocators.ecoLabelForAllProducts):
                        eco_products.append(product_name)
                        print(f"🌿 {product_name}")

                except StaleElementReferenceException:
                    continue

            try:
                next_page = self.driver.find_element(
                    By.CSS_SELECTOR, f"a[aria-label='Page-{page_number + 1}']"
                )

                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});", next_page
                )
                next_page.click()

                self.wait.until(
                    lambda d: d.find_elements(
                        *HomePageLocators.baseItemsProducts
                    )[0].text != first_product_name
                )

                page_number += 1

            except Exception:
                print("✅ No hay más páginas. Fin del recorrido.")
                break

        print(f"\nTotal de productos con label ECO encontrados: {len(eco_products)}")
        return eco_products



    def findFirstOutOfStockProduct(self, max_pages=5, retry_count=3):
        """
        Recorre las páginas hasta encontrar el primer producto con label 'Out of stock'.
        Devuelve un diccionario con nombre, texto del footer y página donde se encontró,
        o None si no se encontró ningún producto fuera de stock.
        """

        page_number = 1

        while page_number <= max_pages:
            print(f"\n📄 Analizando página {page_number}...")

            try:
                # Espera a que se carguen los productos en la página actual
                self.wait.until(EC.presence_of_all_elements_located(HomePageLocators.baseItemsProducts))
                self.wait.until(EC.presence_of_all_elements_located(HomePageLocators.footerCardItems))

                total_items = len(self.driver.find_elements(*HomePageLocators.baseItemsProducts))

                for i in range(total_items):
                    for attempt in range(retry_count):
                        try:
                            # Reubicar los elementos (por si se refrescan)
                            name_el = self.driver.find_elements(*HomePageLocators.baseItemsProducts)[i]
                            footer_el = self.driver.find_elements(*HomePageLocators.footerCardItems)[i]

                            product_name = name_el.text.strip()
                            footer_text = footer_el.text.strip()

                            if "Out of stock" in footer_text:
                                #print(f"❌ Primer producto Out of stock encontrado: {product_name} (página {page_number})")
                                # Devuelve un dict o el propio elemento, según lo que necesites después
                                return {
                                    "nombre": product_name,
                                    "estado": footer_text,
                                    "pagina": page_number,
                                    "elemento": name_el  # por si luego quieres hacer click en él
                                }

                            break  # si todo fue bien, salir del retry loop

                        except StaleElementReferenceException:
                            if attempt < retry_count - 1:
                                time.sleep(0.3)
                                continue
                            else:
                                print(f"⚠️ Elemento {i} dio stale tras {retry_count} intentos, continuando...")
                        except Exception as inner_e:
                            print(f"⚠️ Error inesperado en elemento {i}: {type(inner_e).__name__}")
                            break

                # Si no se encontró en esta página, pasar a la siguiente
                if page_number < max_pages:
                    try:
                        next_page = self.wait.until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, f"a[aria-label='Page-{page_number + 1}']"))
                        )
                        next_page.click()
                        page_number += 1

                        # Esperar que cambie el contenido
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

        print("✅ No se encontró ningún producto 'Out of stock' en todas las páginas.")
        return None

