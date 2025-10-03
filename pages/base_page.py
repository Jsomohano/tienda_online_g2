from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# Tener todas las acciones comunes que voy a necesitar en mis paginas

class BasePage:
    
    ## Constructor
    def __init__(self, driver):
        self.driver = driver
    
    ## Metodos (Interacciones para heredar a mis paginas)
    
    def click_element(self, by_locator):
        element = self.driver.find_element(*by_locator).click()
        
    def enter_text(self, by_locator, text):
        element = self.driver.find_element(*by_locator)
        element.clear()
        element.send_keys(text)
        