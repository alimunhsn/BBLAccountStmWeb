import random
import string
import time
from src.Dashboard.dashboardPage import DashboardPage
from src.Configure.readPropertices import conf
from src.Page.TaskCreatePage import TaskCreatePage
from src.Page.Astm_Login_Page import LoginInPage
from src.Configure.baseSetup import setup


class Test_Job_Create:

    def test_job_update(self, setup):
        self.driver = setup
        time.sleep(1)
        LoginInPage(self.driver).user_login()
        DashboardPage(self.driver).click_task_feature()
        task = TaskCreatePage(self.driver)
        task.click_edit_button("3")
        time.sleep(5)
        # um.click_button_adduser()

        self.driver.close()

    def test_job_create(self, setup):
        self.driver = setup
        time.sleep(1)
        LoginInPage(self.driver).user_login()
        DashboardPage(self.driver).click_task_feature()
        task = TaskCreatePage(self.driver)
        task.new_task_btn()
        task.entry_task_name(conf.get_task_name())
        task.entry_task_tescription(conf.get_task_name())
        task.statement_volume(conf.get_sub_task())
        task.entry_scheme_code(conf.get_scheme_code())
        task.select_statement_type("HALF_YEARLY_ACCOUNT_BALANCE_STATEMENT")
        task.select_year(conf.get_year())
        task.select_month(conf.get_month())
        task.select_job(conf.get_job())
        time.sleep(2)
        task.click_submit_button()
        time.sleep(5)
        # um.click_button_adduser()

        self.driver.close()
