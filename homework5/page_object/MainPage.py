from .BasePage import BasePage
from selenium.webdriver.common.by import By


class MainPageLocators:
    SLIDESHOW = (By.ID, "slideshow0")
    NAME_PRODUCT = (By.CSS_SELECTOR, '#content h1')
    FEATURED_PRODUCTS = (By.CSS_SELECTOR, 'product-layout')
    CURRENCY_DROP_MENU = (By.CSS_SELECTOR, '#form-currency button')
    CURRENCY_EURO = (By.XPATH, '//button[text()="€ Euro"]')
    CURRENCY_POUND_STERLING = (By.XPATH, '//button[text()="£ Pound Sterling"]')
    CURRENCY_DOLLAR = (By.XPATH, '//button[text()="$ US Dollar]')


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def currency_in_main_page(self, currency_path, price, price_path):
        self.drive.find_element()






