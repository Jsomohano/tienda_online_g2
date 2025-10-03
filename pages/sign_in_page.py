from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class SignInPage:
    
## Constructor
    def __init__(self, driver):
        self.driver = driver


## Atributos (Locators)

    email_text_input = (By.ID,"field-email")
    password_text_input = (By.ID, "field-password")
    sign_in_button = (By.ID, "submit-login")


## Metodos (Interacciones con los elementos web)

    def enter_email(self, texto):
        self.driver.find_element(*self.email_text_input).send_keys(texto)
        
    def enter_password(self, texto):
        self.driver.find_element(*self.password_text_input).send_keys(texto)
        
    def click_sign_in(self):
        self.driver.find_element(*self.sign_in_button).click()