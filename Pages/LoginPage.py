from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Config.config import config_data


class LoginPage():

    email = (By.ID,"Email")
    password = (By.ID,"Password")
    login_button = (By.CLASS_NAME,"login-button")

    def __init__(self,driver):
        self.driver = driver
        self.driver.get(config_data.base_url)

    def input_email(self,by_locator,email_value):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by_locator)).clear()
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(by_locator)).send_keys(email_value)

    def input_password(self,by_locator,password_value):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by_locator)).clear()
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(by_locator)).send_keys(password_value)

    def click_submit(self,by_locator):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(by_locator)).click()








