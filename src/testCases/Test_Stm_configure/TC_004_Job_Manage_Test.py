import random
import string
import time
from src.Dashboard.dashboardPage import DashboardPage
from src.Configure.readPropertices import conf
from src.Page.JobCreatePage import JobCreatePage
from src.Page.Astm_Login_Page import LoginInPage
from src.Configure.baseSetup import setup


class Test_Job_Create:

    def test_job_create(self, setup):
        self.driver = setup
        time.sleep(1)
        LoginInPage(self.driver).user_login()
        DashboardPage(self.driver).click_job_feature()
        job = JobCreatePage(self.driver)
        job.add_job_btn()
        job.entry_job_name(conf.get_job_name())
        job.select_statement_type("HALF_YEARLY_ACCOUNT_BALANCE_STATEMENT")
        job.select_schedule_type("FIRST_HALF_YEARLY")
        job.select_stm_year("2023")
        job.click_submit_button()
        time.sleep(5)
        # um.click_button_adduser()

        self.driver.close()
