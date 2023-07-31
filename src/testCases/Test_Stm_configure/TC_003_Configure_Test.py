import random
import string
import time
from src.Dashboard.dashboardPage import DashboardPage
from src.Configure.readPropertices import conf
from src.Page.ConfigurePage import ConfigerPage
from src.Page.Astm_Login_Page import LoginInPage
from src.Configure.baseSetup import setup


class Test_User_Manage:

    letters = string.ascii_lowercase
    usrName = ''.join((random.choice('alimun2234t') for i in range(4)))

    def test_configure_update(self, setup):
        self.driver = setup
        time.sleep(1)
        LoginInPage(self.driver).user_login()
        DashboardPage(self.driver).click_configure_feature()
        cnf = ConfigerPage(self.driver)
        cnf.click_edit_conf()
        cnf.click_submit_btn()
        time.sleep(1)
        self.driver.close()
