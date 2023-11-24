from src.vacancy.abc_vacancy import WorkWithVacancy
from src.vacancy.mixin_for_vacancy.mixin_save_data_about_vacancy import SaveDataAboutVacancy
from src.vacancy.verification_attr.attr_verify import AttrVerify
from src.vacancy.mixin_for_vacancy.mixin_repr_vacancy import ReprVacancy
from src.vacancy.mixin_for_vacancy.mixin_comparison_vacancy import ComparisonVacancy


class HhruVacancy(WorkWithVacancy, AttrVerify, SaveDataAboutVacancy, ReprVacancy, ComparisonVacancy):
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
        self.salary = salary
        self.city = city
