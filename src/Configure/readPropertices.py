from src.Configure import config


class conf:
    @staticmethod
    def getApplicationURl():
        Url = config.BaseUrl  # cfg.get('common', 'BaseUrl')
        return Url

    @staticmethod
    def getUsername():
        username = config.UserName  # cfg.get("common", "UserName")
        return username

    @staticmethod
    def getPassword():
        passwd = config.Password  # cfg.get("common", "Password")
        return passwd

    @staticmethod
    def get_job_name():
        Job_Name = config.JobName  # cfg.get("common", "Password")
        return Job_Name

    @staticmethod
    def get_task_name():
        task_Name = config.TaskName  # cfg.get("common", "Password")
        return task_Name

    @staticmethod
    def get_sub_task():
        task_Name = config.SubTaskCont  # cfg.get("common", "Password")
        return task_Name

    @staticmethod
    def get_scheme_code():
        scheme_code = config.scheme_code  # cfg.get("common", "Password")
        return scheme_code

    @staticmethod
    def get_year():
        year = config.year  # cfg.get("common", "Password")
        return year

    @staticmethod
    def get_month():
        month = config.month  # cfg.get("common", "Password")
        return month

    @staticmethod
    def get_job():
        job = config.job  # cfg.get("common", "Password")
        return job
