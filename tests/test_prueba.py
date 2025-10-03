from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from pages.home_page import HomePage
from pages.sign_in_page import SignInPage

def test_prueba1():
    #Crear un driver
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    home_page = HomePage(driver)
    sign_in_page = SignInPage(driver)
    
    # Paso 1: Abrir el navegador y navegar a la pagina
    driver.get("https://teststore.automationtesting.co.uk/index.php")
    
    
    # Paso 2: Hacer click en Sign In
    home_page.click_sign_in()

    # Paso 3: Ingresar usuario y contrasena
    sign_in_page.enter_email("test@test1.com")
    sign_in_page.enter_password("test123")
    
    # Paso 4: Hacer click en el boton de login
    sign_in_page.click_sign_in()
    
    print("Test finalizado")
    