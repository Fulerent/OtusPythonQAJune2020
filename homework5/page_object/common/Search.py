from ..BasePage import BasePage
from selenium.webdriver.common.by import By


class Locator:
    INPUT_SEARCH = (By.XPATH, '//*[@id="search"]/input')
    BUTTON_SEARCH = (By.CSS_SELECTOR, '#search span')
    TEXT_AFTER_SEARCH = (By.CSS_SELECTOR, '#content > h1')


class Search:

    def __init__(self, driver):
        self.driver = driver

    def input_search(self, query):
        return self.driver.find_element(Locator.INPUT_SEARCH, 2).send_keys(query)

    def click_button_search(self):
        return self.driver.find_element(Locator.BUTTON_SEARCH).click()

