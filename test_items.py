import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_basket_check(browser):
    browser.get(link)
    time.sleep(30)
    assert len(browser.find_element_by_css_selector('button.btn-add-to-basket').get_attribute(
        'value')) != 0, "Add to cart button doesn't exist!"
