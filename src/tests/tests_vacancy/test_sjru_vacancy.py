from src.vacancy.sjru_vacancy import SjruVacancy
from text import REPR_VACANCY

# Data for vacancy number 1
name_1: str = "C++ developer (Telecom)"
url_1: str = "https://sj.ru/vacancy/85423457"
description_1: str = """Совместно с командой предстоит разработка решений от этапа
исследования и прототипирования до вывода в коммерческое использование.
Разработка программного обеспечения для..."""
salary_1: int | dict | None = 60_000
city_1: str = "Санкт-Петербург"

# Vacancy number 1
sjru_vacancy_1 = SjruVacancy(name_1, url_1, description_1, salary_1, city_1)

# Data for vacancy number 2
name_2: str = "C++ developer (Telecom)"
url_2: str = "https://sj.ru/vacancy/85423457"
description_2: str = """Совместно с командой предстоит разработка решений от этапа
исследования и прототипирования до вывода в коммерческое использование.
Разработка программного обеспечения для..."""
salary_2: int | dict | None = 70_000
city_2: str = "Санкт-Петербург"

# Vacancy number 2
sjru_vacancy_2 = SjruVacancy(name_2, url_2, description_2, salary_2, city_2)


def test_sjru_vacancy_repr():
    """Checking the correctness of the output of information about the Vacancy class."""
    assert repr(sjru_vacancy_1) == REPR_VACANCY.format(name=name_1,
                                                       url=url_1,
                                                       description=description_1,
                                                       salary=salary_1,
                                                       city=city_1
                                                       )


def test_sjru_vacancy_comparison():
    # For comparison 'less'
    assert sjru_vacancy_1 < sjru_vacancy_2

    # For comparison 'more'
    assert sjru_vacancy_2 > sjru_vacancy_1

    # For comparison 'less or equal'
    assert sjru_vacancy_1 <= sjru_vacancy_2

    # For comparison 'more or equal'
    assert sjru_vacancy_2 >= sjru_vacancy_1

    # For comparison 'equal'
    assert (sjru_vacancy_1 == sjru_vacancy_2) is False

    # For comparison 'unequal'
    assert sjru_vacancy_2 != sjru_vacancy_1


def test_sjru_vacancy_verify_name_attr():
    # Verify name attribute
    sjru_vacancy_1.name = 'Python'
    assert sjru_vacancy_1.name == 'Python'

    sjru_vacancy_1.name = 123
    assert sjru_vacancy_1.name == ' - '


def test_sjru_vacancy_verify_url_attr():
    # Verify url attribute
    sjru_vacancy_1.url = 'https://sj.ru/vacancy/85423457'
    assert sjru_vacancy_1.url == 'https://sj.ru/vacancy/85423457'

    sjru_vacancy_1.url = 'url'
    assert sjru_vacancy_1.url == ' - '


def test_sjru_vacancy_verify_description_attr():
    # Verify description attribute
    sjru_vacancy_1.description = 'Совместно с командой предстоит разработка решений'
    assert sjru_vacancy_1.description == 'Совместно с командой предстоит разработка решений'

    sjru_vacancy_1.description = 123
    assert sjru_vacancy_1.description == ' - '


def test_sjru_vacancy_verify_salary_attr():
    # Verify salary attribute
    sjru_vacancy_1.salary = 'salary'
    assert sjru_vacancy_1.salary is None

    sjru_vacancy_1.salary = None
    assert sjru_vacancy_1.salary is None

    sjru_vacancy_1.salary = 50_000
    assert sjru_vacancy_1.salary == 50_000

    sjru_vacancy_1.salary = [{'to': 50_000}]
    assert sjru_vacancy_1.salary is None


def test_sjru_vacancy_verify_city_attr():
    # Verify city attribute
    sjru_vacancy_1.city = 'Москва'
    assert sjru_vacancy_1.city == 'Москва'

    sjru_vacancy_1.city = 123
    assert sjru_vacancy_1.city == ' - '
