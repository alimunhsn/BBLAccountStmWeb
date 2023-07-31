import random

from seleniumpagefactory.Pagefactory import PageFactory

from seleniumpagefactory.Pagefactory import PageFactory


class JobCreatePage(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        'Add_NewJob_btn': ('CSS', "a[color='success'] button[type='button']"),
        'entry_jobName': ('Id', "jobName"),
        'statement_Type': ('Id', "statementType"),
        'schedule_type': ('Id', "scheduleType"),
        'select_year': ('Id', "year"),
        'select_role': ('Id', "roleId"),
        'uncheck_hasEmail': ('Id', "hasEmail"),
        'entry_pass': ('Id', "encrptPass"),
        'click_reset': ('Id', "addUserResetButton"),
        'click_submit': ('CSS', "button[type='submit']")

    }

    def add_job_btn(self):
        self.Add_NewJob_btn.click()

    def entry_job_name(self, job):
        self.entry_jobName.set_text(job)

    def select_statement_type(self, value):
        self.statement_Type.select_element_by_value(value)

    def select_schedule_type(self, stype):
        self.schedule_type.select_element_by_value(stype)

    def select_stm_year(self, year):
        self.select_year.select_element_by_value(year)

    def click_submit_button(self):
        self.click_submit.click()
