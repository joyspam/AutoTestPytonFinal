from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import PageObjectLocators
from selenium.common.exceptions import NoAlertPresentException # в начале файла для подсчета кода
import math

class PageObject(BasePage):
    #добавление продукта в корзину
    def add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*PageObjectLocators.ADD_TO_BASKET)
        add_to_basket.click()
    #метод для подсчета кода
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    #проверка что добавился тот же товар
    def should_be_item_in_basket(self): 
        expected_result = self.browser.find_element(*PageObjectLocators.EXPECTED_ITEM_IN_BASKET).text
        actual_result = self.browser.find_element(*PageObjectLocators.ACTUAL_ITEM_IN_BASKET).text
        assert expected_result == actual_result,f'expected {expected_result}, got {actual_result}'

    #проверка что цена совпадает
    def should_be_price_in_basket(self):
        expected_result = self.browser.find_element(*PageObjectLocators.EXPECTED_PRICE).text
        actual_result = self.browser.find_element(*PageObjectLocators.ACTUAL_PRICE).text
        assert expected_result == actual_result,f'expected {expected_result}, got {actual_result}'


    
