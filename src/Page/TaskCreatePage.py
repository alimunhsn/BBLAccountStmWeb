import random

from seleniumpagefactory.Pagefactory import PageFactory

from seleniumpagefactory.Pagefactory import PageFactory


class TaskCreatePage(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        'Add_NewTask_btn': ('CSS', "a[color='success'] button[type='button']"),
        'entry_taskName': ('Id', "TaskName"),
        'Task_Description': ('Id', "TaskDescription"),
        'statement_Volume': ('Id', "statementVolume"),
        'entry_schemeCode': ('Id', "schemeCodeList"),
        'select_statementType': ('Id', "statementType"),
        'year': ('Id', "year"),
        'month': ('Id', "month"),
        'job': ('Id', "job"),
        'click_submit': ('CSS', "button[type='submit']"),
        'edit': ('CSS', "a[href*='#/task-edit']"),
        'details_task': ('CSS', "a[href='#/task-details/78']")

    }

    def new_task_btn(self):
        self.Add_NewTask_btn.click()

    def entry_task_name(self, task):
        self.entry_taskName.set_text(task)

    def entry_task_tescription(self, descript):
        self.Task_Description.set_text(descript)

    def statement_volume(self, vlu):
        self.statement_Volume.set_text(vlu)

    def entry_scheme_code(self, scheme):
        self.entry_schemeCode.set_text(scheme)

    def select_statement_type(self, value):
        self.select_statementType.select_element_by_value(value)

    def select_year(self, year):
        self.year.select_element_by_value(year)

    def select_month(self, month):
        self.month.select_element_by_value(month)

    def select_job(self, job):
        self.job.select_element_by_value(job)

    def click_submit_button(self):
        self.click_submit.click()

    def click_edit_button(self, index):
        self.edit.select_element_by_index(index)
