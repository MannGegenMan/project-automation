import allure
from pages.text_box_page import TextBoxPage
from utilities.data_generator import UserData


@allure.suite("Elements")
@allure.feature("Text Box")
class TestTextBox:
    @allure.title("Проверка заполнения формы Text Box валидными данными")
    @allure.severity(allure.severity_level.NORMAL)
    def test_fill_text_box_form(self, browser):
        # Подготовка данных
        with allure.step("Подготовка данных"):
            test_data = UserData()
            user_data = test_data.generate_text_box()

        # Действия 
        text_box_page = TextBoxPage(browser)

        with allure.step("Открытие страницы Text Box"):
            text_box_page.open()

        with allure.step("Заполнение формы данными"):
            text_box_page.fill_form(user_data)

        # Проверки
        with allure.step("Проверка результатов заполнения формы"):
            result = text_box_page.get_result_data()

            assert result["full_name"] == user_data["full_name"], "Имя не совпадает"
            assert result["email"] == user_data["email"], "Email не совпадает"
            assert (result["current_address"].replace('\n', ' ').strip() == 
                user_data["current_address"].replace('\n', ' ').strip()), "Текущий адрес не совпадает"
            assert (result["permanent_address"].replace('\n', ' ').strip() == 
                user_data["permanent_address"].replace('\n', ' ').strip()), "Постоянный адрес не совпадает"
