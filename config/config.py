import os
import logging
from selenium.webdriver.chrome.options import Options # Класс настройки параметров Chrome браузера
from dotenv import load_dotenv


class Config:
    BASE_URL = "https://demoqa.com/automation-practice-form" # Базовый URL тестируемого сайта
    BROWSER = "chrome"                                       # Тип браузера для тестов
    IMPLICT_WAIT = 10                                        # Неявное ожидание элементов (в секундах)
    EXPLICIT_WAIT = 20                                       # Явное ожидание элементов (в секундах)

    USER_EMAIL = os.getenv('USER_EMAIL', 'default@test.com')
    USER_PASSWORD = os.getenv('USER_PASSWORD', 'defaultpass')


    API_BASE_URL = "https://reqres.in/"                      # Базовый URL для API тестов
    API_TIMEOUT = 10                                         # Таймаут для API запросов
    API_TOKEN = os.getenv('API_TOKEN', '')


    PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
    REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports")
    SCREENSHOTS_DIR = os.path.join(PROJECT_ROOT, "screenshots")


    @staticmethod                                               # Означает, что метод можно вызвать без создания экземпляра класса
    def get_chrome_options():
        chrome_options = Options()
        chrome_options.add_argument("--start-maximizied")       # Запуск браузера в максимальном размере
        chrome_options.add_argument("--no-sandbox")             # Отключение песочницы (важно для CI\CD)
        chrome_options.add_argument("--disable-dev-shm-usage")  # Отключение использования 
        # chrome_options.add_argument("--headless")             # Режим без графического интерфейса

        return chrome_options
    

    @classmethod
    def setup_basic_logging(cls):
        """Базовая настройка логирования только для важных событий"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )