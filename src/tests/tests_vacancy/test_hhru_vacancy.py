from src.vacancy.hhru_vacancy import HhruVacancy
from text import REPR_VACANCY

# Data for vacancy number 1
name_1: str = "C++ developer (Telecom)"
url_1: str = "https://hh.ru/vacancy/85423457"
description_1: str = """Совместно с командой предстоит разработка решений от этапа
исследования и прототипирования до вывода в коммерческое использование.
Разработка программного обеспечения для..."""
salary_1: int | dict | None = 60_000
city_1: str = "Санкт-Петербург"

# Vacancy number 1
hhru_vacancy_1 = HhruVacancy(name_1, url_1, description_1, salary_1, city_1)

# Data for vacancy number 2
name_2: str = "C++ developer (Telecom)"
url_2: str = "https://hh.ru/vacancy/85423457"
description_2: str = """Совместно с командой предстоит разработка решений от этапа
исследования и прототипирования до вывода в коммерческое использование.
Разработка программного обеспечения для..."""
salary_2: int | dict | None = 70_000
city_2: str = "Санкт-Петербург"

# Vacancy number 2
hhru_vacancy_2 = HhruVacancy(name_2, url_2, description_2, salary_2, city_2)


def test_hhru_vacancy_repr():
    """Checking the correctness of the output of information about the Vacancy class"""
    assert repr(hhru_vacancy_1) == REPR_VACANCY.format(name=name_1,
                                                       url=url_1,
                                                       description=description_1,
                                                       salary=salary_1,
                                                       city=city_1
                                                       )


def test_hhru_vacancy_comparison():
    # For comparison 'less'
    assert hhru_vacancy_1 < hhru_vacancy_2

    # For comparison 'more'
    assert hhru_vacancy_2 > hhru_vacancy_1

    # For comparison 'less or equal'
    assert hhru_vacancy_1 <= hhru_vacancy_2

    # For comparison 'more or equal'
    assert hhru_vacancy_2 >= hhru_vacancy_1

    # For comparison 'equal'
    assert (hhru_vacancy_1 == hhru_vacancy_2) is False

    # For comparison 'unequal'
    assert hhru_vacancy_2 != hhru_vacancy_1


def test_hhru_vacancy_verify_name_attr():
    # Verify name attribute
    hhru_vacancy_1.name = 'Python'
    assert hhru_vacancy_1.name == 'Python'

    hhru_vacancy_1.name = 123
    assert hhru_vacancy_1.name == ' - '


def test_hhru_vacancy_verify_url_attr():
    # Verify url attribute
    hhru_vacancy_1.url = 'https://hh.ru/vacancy/85423457'
    assert hhru_vacancy_1.url == 'https://hh.ru/vacancy/85423457'

    hhru_vacancy_1.url = 'url'
    assert hhru_vacancy_1.url == ' - '


def test_hhru_vacancy_verify_description_attr():
    # Verify description attribute
    hhru_vacancy_1.description = 'Совместно с командой предстоит разработка решений'
    assert hhru_vacancy_1.description == 'Совместно с командой предстоит разработка решений'

    hhru_vacancy_1.description = 123
    assert hhru_vacancy_1.description == ' - '


def test_hhru_vacancy_verify_salary_attr():
    # Verify salary attribute
    hhru_vacancy_1.salary = 'salary'
    assert hhru_vacancy_1.salary is None

    hhru_vacancy_1.salary = None
    assert hhru_vacancy_1.salary is None

    hhru_vacancy_1.salary = 50_000
    assert hhru_vacancy_1.salary == 50_000

    hhru_vacancy_1.salary = {
                "from": None,
                "to": 60_000,
                "currency": "RUR",
                "gross": False
            }
    assert hhru_vacancy_1.salary == 60_000

    hhru_vacancy_1.salary = [{'to': 50_000}]
    assert hhru_vacancy_1.salary is None
    
    
def test_hhru_vacancy_verify_city_attr():
    # Verify city attribute
    hhru_vacancy_1.city = 'Москва'
    assert hhru_vacancy_1.city == 'Москва'

    hhru_vacancy_1.city = 123
    assert hhru_vacancy_1.city == ' - '
    