from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_be_product_added_to_basket(self):
        self.should_be_success_message()
        self.should_be_product_name_in_success_message()
        self.should_be_basket_total_equal_to_product_price()

    def should_be_basket_total_equal_to_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL_MESSAGE
        ).text
        assert product_price == basket_total, (
            f"Basket total is '{basket_total}', but product price is '{product_price}'"
        )

    def should_be_product_name_in_success_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_product_name = self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME
        ).text
        assert product_name == message_product_name, (
            f"Message contains '{message_product_name}', but product name is '{product_name}'"
        )

    def should_be_success_message(self):
        assert self.is_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is not disappeared"
