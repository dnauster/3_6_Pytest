import pytest
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_btn_add_basket_language(browser):
    browser.get(link)
    browser.implicitly_wait(10)
    button_basket = browser.find_element_by_css_selector("#add_to_basket_form [type='submit']")
    time.sleep(30)
    assert button_basket, 'Кнопка на форме отсутствует'