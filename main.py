class Employer:
    def __init__(self, work_hours, salary, premium_ratio):
        self.work_hours = work_hours
        self.salary = salary
        self.premium_ratio = premium_ratio

    def get_premium_val(self):
        return self.salary * self.premium_ratio

    def ratio_sal_hours(self):
        return self.salary / self.work_hours


class SeniorEmployer(Employer):
    def __int__(self, work_hours, salary, premium_ratio, work_experience):
        super().__int__(work_hours, salary, premium_ratio)
        self.work_experience = work_experience


class Director(Employer):
    def __int__(self, work_hours, salary, premium_ratio, number_of_subordinates):
        super().__int__(work_hours, salary, premium_ratio)
        self.number_of_subordinates = number_of_subordinates
