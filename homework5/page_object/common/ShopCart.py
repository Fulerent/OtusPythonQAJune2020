from ..BasePage import BasePage
from selenium.webdriver.common.by import By


class Locator:
    CART_BUTTON = (By.CSS_SELECTOR, '#cart button')
    CART_DROP_NOTIFICATION = (By.CSS_SELECTOR, '.dropdown-menu p')
