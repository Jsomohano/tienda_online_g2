from asyncio import wait
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Tener todas las acciones comunes que voy a necesitar en mis paginas

class BasePage:
    
    ## Constructor
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.timout_default)
    
    timout_default = 30
    
    ## Metodos (Interacciones para heredar a mis paginas)
    
    def click_element(self, by_locator, timeout=timout_default):        
        element = self.wait_for_element_to_be_clickable(by_locator,timeout)
        element.click()
        
    def enter_text(self, by_locator, text):
        element = self.driver.find_element(*by_locator)
        element.clear()
        element.send_keys(text)
        
    def wait_for_element_to_be_clickable(self, by_locator, timeout=timout_default):
        self.wait = WebDriverWait(self.driver, timeout)
        return self.wait.until(EC.element_to_be_clickable(by_locator))
        