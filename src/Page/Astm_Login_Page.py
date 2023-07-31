from seleniumpagefactory import PageFactory
from src.Configure.readPropertices import conf


class LoginInPage(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        'user_name': ('NAME', "username"),
        'password': ('NAME', "password"),
        'login_btn': ('CSS', "button[type='submit']")
    }

    def select_username(self, user):
        self.user_name.set_text(user)

    def select_password(self, password):
        self.password.set_text(password)

    def click_login(self):
        self.login_btn.click()

    def user_login(self):
        self.select_username(conf.getUsername())
        self.select_password(conf.getPassword())
        self.click_login()
