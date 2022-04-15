from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    #добавление продукта в корзину
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    #проверка что добавился тот же товар
    EXPECTED_ITEM_IN_BASKET = (By.TAG_NAME, 'h1:nth-child(1)')
    ACTUAL_ITEM_IN_BASKET = (By.CSS_SELECTOR, '.alert-success .alertinner strong')
    #проверка что цена совпадает
    EXPECTED_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    ACTUAL_PRICE = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")