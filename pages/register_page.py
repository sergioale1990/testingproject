from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class RegisterPage:
    PATH = "/auth/register"

    FIRSTNAME = (By.ID, "first_name")
    LASTNAME = (By.ID, "last_name")
    DATE_OF_BIRTH = (By.ID, "dob")
    STREET = (By.ID, "street")
    POSTAL_CODE = (By.ID, "postal_code")
    CITY = (By.ID, "city")
    STATE = (By.ID, "state")
    PHONE = (By.ID, "phone")
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    SUBMIT = By.CSS_SELECTOR, "[data-test='register-submit'], button[type='submit']"
    country_dropdown = (By.ID, "country")

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open(self):
        self.driver.get(self.base_url + self.PATH)

    def register(self, first_name, last_name, date_of_birth, street, postal_code, city, state, phone, email, password):
        d = self.driver
        d.find_element(*self.FIRSTNAME).send_keys(first_name)
        d.find_element(*self.LASTNAME).send_keys(last_name)
        d.find_element(*self.DATE_OF_BIRTH).send_keys(date_of_birth)
        d.find_element(*self.STREET).send_keys(street)
        d.find_element(*self.POSTAL_CODE).send_keys(postal_code)
        d.find_element(*self.CITY).send_keys(city)
        d.find_element(*self.STATE).send_keys(state)
        d.find_element(*self.PHONE).send_keys(phone)
        country = "Albania"
        country_select = d.find_element(*self.country_dropdown)
        select = Select(country_select)
        select.select_by_visible_text(country)
        d.find_element(*self.EMAIL).send_keys(email)
        d.find_element(*self.PASSWORD).send_keys(password)
        d.find_element(*self.SUBMIT).click()
    def redirect_to_login_page(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.any_of(
                    EC.url_contains("/auth/login"),
                )
            )
        except:
            pass
