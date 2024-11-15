import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from allure_commons.types import AttachmentType
from datetime import datetime


@pytest.fixture(scope="function")
# scope="function" означает, что драйвер будет создаваться для каждого теста заново
def browser():
    # Инициализация драйвера Chrome с автоматической загрузкой нужной версии
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #Развертывание окна браузера на весь экран
    browser.maximize_window()
    # Добавляем информацию о браузере в отчет
    allure.attach(
        name="Browser information",
        body=f"Browser: Chrome\nVersion: {browser.capabilities['browserVersion']}",
        attachment_type=AttachmentType.TEXT
    )
    # yield позволяет выполнить код до и после теста
    yield browser
    # Делаем скриншот после каждого теста
    allure.attach(
        browser.get_screenshot_as_png(),
        name="finish_test",
        attachment_type=AttachmentType.PNG
    )
    # После завершения теста браузер будет закрыт
    browser.quit()


# Добавляем обработчик для скриншотов при падении тестов
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        if report.failed:
            browser = item.funcargs["browser"]
            take_screenshot(browser)

# Функция для создания скришота
def take_screenshot(browser):
    allure.attach(
        browser.get_screenshot_as_png(),
        name=f"failure_screenshot_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}",
        attachment_type=AttachmentType.PNG
    )