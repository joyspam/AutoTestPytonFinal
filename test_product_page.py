from .pages.product_page import PageObject
import pytest #чтобы работали маркированные тесты



@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail(reason="error on page")),
                                  8, 9])

#продукт можно добавить в корзину
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = PageObject(browser,link)
    page.open()
    page.add_product_to_basket() #добавление продукта в корзину
    page.solve_quiz_and_get_code() #метод для подсччета кода
    page.should_be_item_in_basket() #добавился тот же товар
    page.should_be_price_in_basket() #цена совпадает с добавленным товаром


        

