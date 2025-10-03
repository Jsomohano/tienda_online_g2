from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class HomePage:
    
## Constructor
    def __init__(self, driver):
        self.driver = driver


## Atributos (Locators)

    sign_in_button = (By.CSS_SELECTOR,".user-info")
    cart_button = (By.XPATH, "//div[@id='_desktop_cart']/div")


## Metodos (Interacciones con los elementos web)
    def click_sign_in(self):
        self.driver.find_element(*self.sign_in_button).click()
        
    def click_cart(self):
        self.driver.find_element(*self.cart_button).click()
        
        
        
# Crear un folder de su proyecto
# Crear un ambiente virtual
# Instalar las librerias necesarias (selenium, webdriver-manager, pytest)
# Crear los folders
# Verificar que tengan las librerias instaladas
# Crear el POM de la pagina HOME