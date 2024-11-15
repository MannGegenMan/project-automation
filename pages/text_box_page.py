from pages.base_page import BasePage
from locators.text_box_locators import TextBoxLocators


class TextBoxPage(BasePage): # TextBox наследуется от BasePage
    def __init__(self, browser): # Конструктор класса, который вызывается при создании объекта
        super().__init__(browser) # Вызываем конструктор родительского класса (BasePage)
        self.URL = "https://demoqa.com/text-box"

    def open(self):
        """Открытие страницы text box"""
        self.browser.get(self.URL)

    def fill_form(self, user_data):
        """
        Заполняем форму
        :param user_data: словарь с данными из TestData.generate_text_box()
        """
        self.input_text(TextBoxLocators.FULL_NAME_INPUT, user_data["full_name"])
        self.input_text(TextBoxLocators.EMAIL_INPUT, user_data["email"])
        self.input_text(TextBoxLocators.CURRENT_ADDRESS_INPUT, user_data["current_address"])
        self.input_text(TextBoxLocators.PERMANENT_ADDRESS_INPUT, user_data["permanent_address"])
        self.click_element(TextBoxLocators.SUBMIT_BUTTON)

    def get_result_data(self):
        """Получаем данные из результата заполнения формы"""
        def extract_value(text):
            """Вспомогательная функция для извлечения значения после двоеточия"""
            return text.split(":")[1].strip() if ":" in text else ""

        return {
            "full_name": extract_value(self.get_text(TextBoxLocators.NAME_RESULT)),
            "email": extract_value(self.get_text(TextBoxLocators.EMAIL_RESULT)),
            "current_address": extract_value(self.get_text(TextBoxLocators.CURRENT_ADDRESS_RESULT)),
            "permanent_address": extract_value(self.get_text(TextBoxLocators.PERMANENT_ADDRESS_RESULT))
        }
        