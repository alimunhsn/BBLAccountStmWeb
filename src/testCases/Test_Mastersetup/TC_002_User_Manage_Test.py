import random
import string
import time
from src.Dashboard.dashboardPage import DashboardPage
from src.Configure.readPropertices import conf
from src.Page.UserManagementPage import UserManagementPage
from src.Page.Astm_Login_Page import LoginInPage
from src.Configure.baseSetup import setup


class Test_User_Manage:
    fullname = "MD Alimun Hasan"
    # usrName = "alimun1193"
    # usrname = random.randint(alimun , 10001)
    role = "3"
    usrStatus = "0"
    usrType = "0"
    userPass = "Brac@1234."
    num = random.randint(1001, 10010)
    userPin = "11234"
    department = "BBLSQA"

    letters = string.ascii_lowercase
    usrName = ''.join((random.choice('alimun2234t') for i in range(4)))

    def test_user_page_reset(self, setup):
        self.driver = setup
        time.sleep(1)
        LoginInPage(self.driver).user_login()
        DashboardPage(self.driver).click_user_module_module()
        um = UserManagementPage(self.driver)
        um.add_user_btn()
        um.entry_fullname(self.fullname)
        um.entry_user_pin(self.num)
        um.entry_department(self.department)
        um.entry_add_username(self.usrName)
        um.click_usr_email()
        time.sleep(1)
        um.select_role_name(self.role)
        um.entry_user_password(conf.getPassword())
        um.click_button_adduser()
        # um.click_button_adduser()
        time.sleep(1)
        self.driver.close()
