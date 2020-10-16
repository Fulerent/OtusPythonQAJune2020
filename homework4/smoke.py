import pytest
import selenium


def test_opencart(web_driver, page_url):
    wd = web_driver
    wd.get(page_url)
    assert wd.title == 'Your Store'
