from .pages.product_page import ProductPage
import pytest #чтобы работали маркированные тесты



@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail(reason="error on page")),
                                  8, 9])

#продукт можно добавить в корзину
@pytest.mark.skip(reason="promo is over")
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser,link)
    page.open()
    page.add_product_to_basket() #добавление продукта в корзину
    page.solve_quiz_and_get_code() #метод для подсчета кода
    page.should_be_item_in_basket() #добавился тот же товар
    page.should_be_price_in_basket() #цена совпадает с добавленным товаром

#негативные проверки

#нет сообщения об успехе при добавлении товара в корзину (элемент не появляется в течении заданного времени)
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()  # добавление продукта в корзину
    page.should_not_be_success_message()

#нет сообщения об успехе при открытии страницы (элемент не появляется в течении заданного времени)
@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

#нет сообщения об успехе при добавлении товара в корзину (#элемент исчезает)
@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()  # добавление продукта в корзину
    page.should_be_disappeared_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()