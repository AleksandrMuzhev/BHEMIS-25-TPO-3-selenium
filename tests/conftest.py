import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

@pytest.fixture
def driver():
    """
    Фикстура для подготовки браузера для теста
    """
    options = Options()
    options.add_argument("--headless") # Для сервера/CI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.get("http://localhost:9999")
    yield driver
    driver.quit()