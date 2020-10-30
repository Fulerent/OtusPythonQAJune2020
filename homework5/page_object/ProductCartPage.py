from .BasePage import BasePage
from selenium.webdriver.common.by import By


class ProductCartPage(BasePage):
    url_product = "/macbook"
    wish_list_assert_text = 'Wish List (1)'

    NAME_PRODUCT = (By.CSS_SELECTOR, '#content h1')
    BUTTON_ADD_WISH_LIST = (By.XPATH, '//button[@data-original-title="Add to Wish List"]')
    WISH_LIST = (By.CSS_SELECTOR, '#wishlist-total span')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '#content li h2')
    BUTTON_ADD_TO_CART = (By.ID, 'Add to Cart')
    SHOPPING_CART = (By.ID, 'cart-total')
    AMOUNT_OF_GOODS = (By.ID, 'input-quantity')

    # def add_wish_list(self, text):
    #     self._find_element(self.BUTTON_ADD_WISH_LIST).click()
    #     a = self._text_to_be_present_in_element_value(self.WISH_LIST,text)
    #     return a

    def save_price(self, locator=PRICE_PRODUCT):
        return self._find_element(locator).text

    def click(self, locator):
        self._find_element(locator).click()
        return self

    def get_element_text(self, locator):
        return self._find_element(locator).text

    def input_data(self, locator, value):
        self._input(locator, value)
        return self


