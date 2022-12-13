from selenium.webdriver.common.by import By


class locator_Lista():
    contador = 0
    indice = 0

    def __init__(self, driver):
        self.driver = driver
        self.lista_fhios = (By.XPATH, '//*[contains(text(),"Fhios")]')








    def buscar_coincidencias(self, palabra, lista):
        self.lista = self.driver.find_elements(*lista)
        if self.indice <= len(self.lista) - 1:
            if self.lista[self.indice].get_attribute("innerText").__contains__(palabra):
                self.contador = self.contador + 1
                self.indice = self.indice + 1
                return self.buscar_coincidencias(palabra, lista)
        print("La palabra Fhios aparece {} veces en la página web.".format(self.contador))