from Config.config import config_data
from Pages.LoginPage import LoginPage
from Tests.BaseTest import Test_Base


class Test_Login(Test_Base):

    def test_login(self):

        self.loginpage = LoginPage(self.driver)
        self.loginpage.input_email(LoginPage.email,config_data.username)
        self.loginpage.input_password(LoginPage.password,config_data.password)
        self.loginpage.click_submit(LoginPage.login_button)

