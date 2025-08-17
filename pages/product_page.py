from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    NAME = (By.CSS_SELECTOR, "[data-test='product-name'], h1[data-test='page-title']")
    ADD_TO_CARD = (By.XPATH, "//button[@data-test='add-to-cart']")
    MESSAGE_SUCCESS = (By.CSS_SELECTOR, "[role='alert'], .toast-message")

    def __init__(self, driver):
        self.driver = driver

    def assert_loaded_with_name(self, expected_name: str, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.NAME, expected_name)
        )

    def add_to_cart(self):
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_TO_CARD)
        )
        add_to_cart_button.click()

    def wait_added_to_cart_message(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.MESSAGE_SUCCESS))
