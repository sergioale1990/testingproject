# conftest.py
import pytest, os, random, string
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = os.getenv("BASE_URL", "https://practicesoftwaretesting.com")

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="session")
def browser():
    chrome_opts = Options()
    # chrome_opts.add_argument("--headless=new")  # opcional
    chrome_opts.add_argument("--window-size=1366,900")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_opts)

    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def unique_email(prefix="autotest"):
    import string, random
    suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{prefix}{suffix}@example.com"

@pytest.fixture
def make_unique_email():
    return unique_email()
