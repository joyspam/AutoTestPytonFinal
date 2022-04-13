from .pages.product_page import PageObject

#продукт можно добавить в корзину
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = PageObject(browser,link)
    page.open()
    page.add_product_to_basket() #добавление продукта в корзину
    page.solve_quiz_and_get_code() #метод для подсччета кода
    page.should_be_item_in_basket() #добавился тот же товар
    page.should_be_price_in_basket() #цена совпадает с добавленным товаром


        

