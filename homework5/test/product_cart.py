import pytest
import time
from homework5.page_object.ProductCartPage import ProductCartPage


def test_h1(browser):
    browser.open(ProductCartPage.url_product)
    text = ProductCartPage(browser) \
        .get_element_text(ProductCartPage.NAME_PRODUCT)
    assert text == "MacBook"


def test_wish_list(browser):
    browser.open(ProductCartPage.url_product)
    text = ProductCartPage(browser)\
        .click(ProductCartPage.BUTTON_ADD_WISH_LIST)\
        .get_element_text(ProductCartPage.WISH_LIST)
    assert ProductCartPage.wish_list_assert_text in text


def test_add_cart(browser):
    browser.open(ProductCartPage.url_product)
    price_product = ProductCartPage(browser).save_price()
    price_shop_cart = ProductCartPage(browser)\
        .click(ProductCartPage.BUTTON_ADD_TO_CART)\
        .get_element_text(ProductCartPage.SHOPPING_CART)

    assert price_shop_cart == "1 item(s) - " + price_product


@pytest.mark.parametrize("count", (2, 3, 4, 10))
def test_add_cart_many(browser, count):
    browser.open(ProductCartPage.url_product)
    count_items = ProductCartPage(browser)\
        .input_data(ProductCartPage.AMOUNT_OF_GOODS, count)\
        .click(ProductCartPage.BUTTON_ADD_TO_CART)\
        .get_element_text(ProductCartPage.SHOPPING_CART)
    assert f"{count} item(s) -" in count_items


# @pytest.mark.parametrize("url", ('#content > div > div.col-sm-4 > div.rating > p > a:nth-child(6)',
#                                  '#content > div > div.col-sm-4 > div.rating > p > a:nth-child(7)',
#                                  '#content > div > div.col-sm-8 > ul.nav.nav-tabs > li:nth-child(3) > a'))
# def test_error_add_comment(url, web_driver, page_url):
#     wd = web_driver
#     wd.get(page_url + url_category)
#     wd.find_element_by_css_selector(url).click()
#     wd.find_element_by_id("input-name").send_keys("Kirill")
#     wd.find_element_by_id("input-review").send_keys("Текст длиной более 25 символоа!!!!!!!!!!!!!")
#     wd.find_element_by_id("button-review").click()
#     time.sleep(1)
#     error_text = wd.find_element_by_css_selector("#form-review > div.alert.alert-danger.alert-dismissible").text
#     assert error_text == "Warning: Please select a review rating!"
#
#


