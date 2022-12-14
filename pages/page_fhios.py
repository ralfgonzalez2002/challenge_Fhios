from selenium.webdriver.common.by import By


class locator_Lista():
    contador = 0
    contador_global = 0
    indice = 0
    indice2 = 0

    def __init__(self, driver):
        self.driver = driver
        self.lista_fhios = (By.XPATH, '//*[contains(text(),"Fhios")]')
        self.lista_btns = [(By.ID, "menu-item-5875"), (By.ID, "menu-item-7070"), (By.ID, "menu-item-5876"),
                           (By.ID, "menu-item-7034"), (By.ID, "menu-item-70")]

    def buscar_coincidencias(self, palabra, lista):
        self.lista = self.driver.find_elements(*lista)
        if self.indice <= len(self.lista) - 1:
            if self.lista[self.indice].get_attribute("innerText").__contains__(palabra):
                self.contador = self.contador + 1
                self.indice = self.indice + 1
                return self.buscar_coincidencias(palabra, lista)
            else:
                self.indice = self.indice + 1
                return self.buscar_coincidencias(palabra, lista)
        return self.contador

    def change_page(self, lista_pages):
        if self.indice2 <= len(lista_pages) - 1:
            btn = self.driver.find_element(*lista_pages[self.indice2])
            btn.click()
            self.indice2 = self.indice2 + 1
            self.contador_global = self.contador_global + self.buscar_coincidencias("Fhios", self.lista_fhios)
            return self.change_page(lista_pages)

    def cosa(self, palabra, lista, lista_pages):
        self.contador_global = self.contador_global + self.buscar_coincidencias(palabra, lista)
        self.change_page(lista_pages)
        print("La palabra Fhios aparece {} veces en la página web.".format(self.contador_global))