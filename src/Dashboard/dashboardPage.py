from seleniumpagefactory.Pagefactory import PageFactory


class DashboardPage(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        'User_module': ('LINK_TEXT', "Users"),
        'Task_Feature': ('LINK_TEXT', "Task"),
        'Configure_Queue_feature': ('LINK_TEXT', "Statement Conf"),
        'Job_create_feature': ('CSS', "a[href='#/jobs']"),
    }

    def click_user_module_module(self):
        self.User_module.click()

    def click_reconciliation_queue_module(self):
        self.Reconciliation_Queue_module.click()

    def click_configure_feature(self):
        self.Configure_Queue_feature.click()

    def click_job_feature(self):
        self.Job_create_feature.click()

    def click_task_feature(self):
        self.Task_Feature.click()
