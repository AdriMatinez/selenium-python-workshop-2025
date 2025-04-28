from selenium.webdriver.common.by import By
import time


class SearchPage():
    PRODUCT_NAME = (By.XPATH, "/html/body/header/div/div[2]/form/input")
    SEARCH_BUTTON = (By.XPATH, "/html/body/header/div/div[2]/form/button")
    
    def __init__(self, driver):
        self.driver = driver
        
    def search_product(self, product_name):
        self.driver.find_element(*self.PRODUCT_NAME).send_keys(product_name)
        self.driver.find_element(*self.SEARCH_BUTTON).click()
