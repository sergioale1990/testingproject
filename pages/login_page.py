from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    PATH = "/auth/login"

    EMAIL = (By.CSS_SELECTOR, "input[type='email'], input[name='email']")
    PASSWORD = (By.CSS_SELECTOR, "input[type='password'], input[name='password']")
    SUBMIT = (By.CSS_SELECTOR, "[data-test='login-submit'], button[type='submit']")
    REGISTER_LINK = (By.LINK_TEXT, "Register your account")
    TITLE = (By.XPATH, "h1[@data-test='page-title']")

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open(self):
        self.driver.get(self.base_url + self.PATH)

    def go_to_register(self):
        try:
            self.driver.find_element(*self.REGISTER_LINK).click()
        except:
            self.driver.find_element(By.PARTIAL_LINK_TEXT, "Register").click()

    def login(self, email, password):
        self.driver.find_element(*self.EMAIL).clear()
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.SUBMIT).click()

    def assert_logged_in(self, timeout=10):
        EC.presence_of_element_located(self.TITLE)
