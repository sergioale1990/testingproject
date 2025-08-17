from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    PATH = "/"
    PRODUCT_CARDS = (By.CSS_SELECTOR, "a.card[data-test^='product-']")

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open(self):
        self.driver.get(self.base_url + self.PATH)

    def _card_by_name(self, name: str):
        return (By.XPATH, f"//h5[@data-test='product-name' and normalize-space()='{name}']"
                          f"/ancestor::a[contains(@class,'card')]")

    def click_product_by_name(self, name: str, timeout=10):
        # Espera a que haya cards y luego busca la que coincide por texto del <h5>
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(self.PRODUCT_CARDS))
        el = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self._card_by_name(name))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
        try:
            el.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", el)
