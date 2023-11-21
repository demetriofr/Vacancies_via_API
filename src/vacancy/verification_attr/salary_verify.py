class SalaryVerify:
    """Verification the salary attribute of the Vacancy class"""

    def __init__(self, salary):
        self.salary = salary

    @classmethod
    def verify_salary(cls, salary):
        if isinstance(salary, dict):
            if salary["from"] >= salary["to"]:
                return salary["from"]
            else:
                return salary["to"]
        elif isinstance(salary, (int, float)):
            return salary
        else:
            return None

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        salary = self.verify_salary(salary)
        self.__salary = salary
