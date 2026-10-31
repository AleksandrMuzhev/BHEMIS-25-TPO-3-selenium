from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from ..data.test_data import name


def test_should_send_form(driver):
    # 1. Вводим имя
    driver.find_element(By.CSS_SELECTOR, "[data-test-id=name] input").send_keys(name)

    # 2. Вводим телефон
    driver.find_element(By.CSS_SELECTOR, "[data-test-id=phone] input").send_keys("+79120009999")

    # 3. Ставим чекбокс
    driver.find_element(By.CLASS_NAME, "checkbox__box").click()

    # 4. Нажимаем кнопку
    driver.find_element(By.CLASS_NAME, "button").click()

    # 5. Ждем появления сообщения об успехе (используем правильное ожидание вместо sleep)
    success_msg = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test-id=order-success]"))
    ).text.strip()

    # 6. Проверяем результат
    assert success_msg == "Ваша заявка успешно отправлена! Наш менеджер свяжется с вами в ближайшее время."
