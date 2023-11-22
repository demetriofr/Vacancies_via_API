from src.vacancy.abc_vacancy import WorkWithVacancy
from src.vacancy.verification_attr.attr_verify import AttrVerify
from src.vacancy.mixin_repr_vacancy import ReprVacancy
from src.vacancy.mixin_comparison_vacancy import ComparisonVacancy


class HhruVacancy(WorkWithVacancy, AttrVerify, ReprVacancy, ComparisonVacancy):
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

    @classmethod
    def get_data_about_vacancy(cls, vacancy_from_json: dict) -> dict:
        """Get data about vacancy from json using JSON from the cache"""

        cls.name = vacancy_from_json['name']
        cls.url = vacancy_from_json['alternate_url']
        cls.description = vacancy_from_json['snippet']['responsibility']
        cls.salary = vacancy_from_json['salary']
        cls.city = vacancy_from_json['area']['name']

        vacancy_n = {
            'name': cls.name,
            'url': cls.url,
            'description': cls.description,
            'salary': cls.salary,
            'city': cls.city
            }

        return vacancy_n
