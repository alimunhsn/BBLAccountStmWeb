from seleniumpagefactory import PageFactory

from src.Configure.readPropertices import conf


class ConfigerPage(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        'Edit_conf_btn': ('CSS', "a[href='#/statement-configure-edit/2']"),
        'password': ('NAME', "password"),
        'submit_btn': ('CSS', "button[type='submit']")
    }

    def click_edit_conf(self):
        self.Edit_conf_btn.click()

    def click_submit_btn(self):
        self.submit_btn.click()
