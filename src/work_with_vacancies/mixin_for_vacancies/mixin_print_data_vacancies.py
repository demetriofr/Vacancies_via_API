from text import PRINT_VACANCIES
from src.data_work.work_with_json import WorkWithJson


class PrintDataVacancies:
    """Print vacancies from a JSON file."""

    @classmethod
    def print_data_vacancies(cls, path_json):
        """Print vacancies from a JSON file."""

        cache_json = WorkWithJson.read_data(path_json)

        for vacancy_with_cache_json in cache_json:
            print(PRINT_VACANCIES.format(
                unique=vacancy_with_cache_json["unique"],
                name=vacancy_with_cache_json["name"],
                url=vacancy_with_cache_json["url"],
                description=vacancy_with_cache_json["description"],
                salary=vacancy_with_cache_json["salary"],
                city=vacancy_with_cache_json["city"]
            ))
