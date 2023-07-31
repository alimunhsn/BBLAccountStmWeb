import random

from seleniumpagefactory.Pagefactory import PageFactory

from seleniumpagefactory.Pagefactory import PageFactory


class UserManagementPage(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        'Add_user_btn': ('CSS', "a[color='info'] button[type='button']"),
        'Full_Name': ('Id', "name"),
        'user_pin': ('Id', "pin"),
        'entry_dept': ('Id', "department"),
        'add_Username': ('Id', "username"),
        'select_role': ('Id', "roleId"),
        'uncheck_hasEmail': ('Id', "hasEmail"),
        'entry_pass': ('Id', "encrptPass"),
        'click_reset': ('Id', "addUserResetButton"),
        'click_adduser': ('CSS', "button[type='submit']")

    }

    def add_user_btn(self):
        self.Add_user_btn.click()

    def entry_fullname(self, fullname):
        self.Full_Name.set_text(fullname)

    def entry_user_pin(self, pin):
        self.user_pin.set_text(pin)

    def entry_department(self, depart):
        self.entry_dept.set_text(depart)

    def entry_add_username(self, user):
        self.add_Username.set_text(user)

    def select_role_name(self, role):
        self.select_role.select_element_by_value(role)

    def click_usr_email(self):
        self.uncheck_hasEmail.click()

    def entry_user_password(self, userpass):
        self.entry_pass.set_text(userpass)

    def click_button_reset(self):
        self.click_reset.click()

    def click_button_adduser(self):
        self.click_adduser.click()
