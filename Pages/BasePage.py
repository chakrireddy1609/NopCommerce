from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self,driver):
        self.driver = driver

    def click_element(self,by_locator):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(by_locator)).click()

    def send_keys(self,by_locator,text):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(by_locator)).send_keys(text)

    def page_title(self,title):
        WebDriverWait(self.driver,10).until(expected_conditions.title_is(title))
        return self.driver.title

    def clear_field(self,by_locator):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(by_locator)).clear()



