import unittest
from selenium import webdriver
from pages.page_fhios import locator_Lista as Page_Fhios


class Item7(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(executable_path=r"C:\challenge_Fhios\driver\chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.fhios.es/")
        self.page_Fhios = Page_Fhios(self.driver)


    def test_buscar_coincidencias(self):
        self.page_Fhios.cosa("Fhios", self.page_Fhios.lista_fhios, self.page_Fhios.lista_btns)



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()