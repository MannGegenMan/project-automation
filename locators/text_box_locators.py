from selenium.webdriver.common.by import By


class TextBoxLocators:
    FULL_NAME_INPUT = (By.ID, "userName")
    EMAIL_INPUT = (By.ID, "userEmail")
    CURRENT_ADDRESS_INPUT = (By.ID, "currentAddress")
    PERMANENT_ADDRESS_INPUT = (By.ID, "permanentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")

    NAME_RESULT = (By.XPATH, "//p[@id='name']")
    EMAIL_RESULT = (By.XPATH, "//p[@id='email']")
    CURRENT_ADDRESS_RESULT = (By.XPATH, "//p[@id='currentAddress']")
    PERMANENT_ADDRESS_RESULT = (By.XPATH, "//p[@id='permanentAddress']")
    
    # Дополнительно добавим локатор для блока с результатами
    OUTPUT_BLOCK = (By.ID, "output")
