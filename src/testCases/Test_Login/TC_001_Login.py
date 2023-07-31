import time

from src.Configure import config
from src.Page.Astm_Login_Page import LoginInPage
from src.Configure.baseSetup import setup


class Test_TC001_Login():
    username = config.UserName
    password = config.Password

    def test_login(self, setup):
        self.driver = setup
        self.lp = LoginInPage(self.driver)
        self.lp.select_username(self.username)
        self.lp.select_password(self.password)
        self.lp.click_login()
        self.driver.quit()
