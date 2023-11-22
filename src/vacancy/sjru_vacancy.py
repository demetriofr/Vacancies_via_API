from src.vacancy.abc_vacancy import WorkWithVacancy
from src.vacancy.verification_attr.attr_verify import AttrVerify
from src.vacancy.mixin_repr_vacancy import ReprVacancy
from src.vacancy.mixin_comparison_vacancy import ComparisonVacancy


class SjruVacancy(WorkWithVacancy, AttrVerify, ReprVacancy, ComparisonVacancy):
    """Work with vacancy with superjob.ru"""

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

    def get_data_about_vacancy(self, vacancy_from_json: dict) -> dict:
        """Get data about vacancy from json using JSON from the cache"""

        self.name = vacancy_from_json['profession']
        self.url = vacancy_from_json['link']
        self.description = vacancy_from_json['candidat']
        self.salary = vacancy_from_json['payment_from']
        self.city = vacancy_from_json['town']['title']

        vacancy_n = {
            'name': self.name,
            'url': self.url,
            'description': self.description,
            'salary': self.salary,
            'city': self.city
            }

        return vacancy_n
