import pytest
from homework5.page_object.Login import Login
import time


@pytest.mark.parametrize("login_password", Login.login_password)
def test_error_login(browser, login_password):
    browser.open(Login.url_category)
    error_text = Login(browser).\
        input_data(Login.INPUT_EMAIL, login_password[0])\
        .input_data(Login.INPUT_PASSWORD, login_password[1])\
        .click(Login.BUTTON_LOGIN)\
        .get_element_text(Login.NOTIFICATION_ERROR_LOGIN)

    assert error_text == Login.error_text_notification


def test_button_new_customer(browser):
    browser.open(Login.url_category)
    h1_register = Login(browser).\
        click(Login.NEW_USER).\
        get_element_text(Login.H1_REGISTER_ACCOUNT)

    assert h1_register == Login.h1_register_template


def test_forgotten_password_link(browser):
    browser.open(Login.url_category)
    h1_password_recovery = Login(browser).click(Login.FORGOTTEN_PASSWORD_LINK)\
        .get_element_text(Login.H1_REGISTER_ACCOUNT)

    assert h1_password_recovery == Login.h1_password_recovery_template


def test_login(browser):
    browser.open(Login.url_category)
    new_user = Login(browser).click(Login.NEW_USER)\
        .input_data(Login.FIRST_NAME, Login.name)\
        .input_data(Login.LAST_NAME, Login.name)\
        .input_data(Login.EMAIL, Login.email)\
        .input_data(Login.TELEPHONE, Login.telephone)\
        .input_data(Login.INPUT_PASSWORD, Login.password)\
        .input_data(Login.CONFIRM_PASSWORD, Login.password)\
        .click(Login.NEWSLETTER_CHECKBOX_YES)\
        .click(Login.PRIVACY_POLICY)\
        .click(Login.FINISH_REGISTER)
    new_user.get_element_text(Login.H1_REGISTER_ACCOUNT)
    time.sleep(5)
    assert new_user == Login.h1_new_account_register
#TODO почему-то не успевает заполнять поля, разобраться с ожиданием
#
#
# def test_forgotten_error(web_driver, page_url):
#     wd = web_driver
#     wd.get(page_url + url_category)
#     wd.find_element_by_css_selector('#content > div > div:nth-child(2) > div > form > div:nth-child(2) > a').click()
#     time.sleep(1)
#     wd.find_element_by_id("input-email").click()
#     wd.find_element_by_id("input-email").send_keys(email)
#     wd.find_element_by_css_selector("#content > form > div > div.pull-right > input").click()
#     time.sleep(1)
#     error_text = wd.find_element_by_css_selector("#account-forgotten > div.alert.alert-danger.alert-dismissible").text
#     assert "Warning: The E-Mail Address was not found in our records, please try again!" in error_text
