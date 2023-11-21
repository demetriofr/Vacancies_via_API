from src.vacancy.abc_vacancy import WorkWithVacancy
from src.vacancy.verification_attr.attr_verify import AttrVerify
from text import REPR_VACANCY


class HhruVacancy(WorkWithVacancy, AttrVerify):
    """Work with vacancy with hh.ru"""

    def __init__(self,
                 name: str,
                 url: str,
                 description: str,
                 salary: int | dict | None,
                 city: str
                 ):
        self.name = name
        self.url = url
        self.description = description
        self.__salary = salary
        self.city = city

    def __repr__(self):
        return REPR_VACANCY.format(name=self.name,
                                   url=self.url,
                                   description=self.description,
                                   salary=self.__salary,
                                   city=self.city
                                   )

    def __lt__(self, other):
        """For comparison 'less'"""
        if isinstance(other, self.__class__):
            return self.__salary < other.__salary

    def __gt__(self, other):
        """For comparison 'more'"""
        if isinstance(other, self.__class__):
            return self.__salary > other.__salary

    def __le__(self, other):
        """For comparison 'less or equal'"""
        if isinstance(other, self.__class__):
            return self.__salary <= other.__salary

    def __ge__(self, other):
        """For comparison 'more or equal'"""
        if isinstance(other, self.__class__):
            return self.__salary >= other.__salary

    def __eq__(self, other):
        """For comparison 'equal'"""
        if isinstance(other, self.__class__):
            return self.__salary == other.__salary

    def __ne__(self, other):
        """For comparison 'unequal'"""
        if isinstance(other, self.__class__):
            return self.__salary != other.__salary
