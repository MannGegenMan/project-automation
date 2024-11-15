from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10) # Явное ожидание 10 секунд

    def find_element(self, locator):
        """Найти элемент по локатору"""
        return self.wait.until(EC.presence_of_element_located(locator))
        
    def click_element(self, locator):
        """Кликнуть по элементу"""
        element = self.find_element(locator)
        # Прокручиваем к элементу
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        #Ждем небольшую паузу после прокрутки
        time.sleep(1)
        element.click()

    def input_text(self, locator, text):
        """Ввести текст"""
        element = self.find_element(locator)
        element.clear() # Сначала очищаем поле
        element.send_keys(text)

    def get_text(self, locator):
        """Получить текст элемента"""
        return self.find_element(locator).text
