from src.data_work.work_with_json import WorkWithJson
from src.vacancy.hhru_vacancy import HhruVacancy
from src.work_with_vacancies.mixin_for_vacancies.mixin_save_data_vacancies import SaveDataVacancies


class DeleteCutNVacancies(SaveDataVacancies):
    """Delete N vacancies by list"""

    @classmethod
    def delete_n_vacancies(cls, del_list: list, path_json: str, path_json_del_result: str) -> None:
        """Delete n vacancies by list in which the vacancies numbers are transmitted"""

        unique = 1
        vacancies: list = []
        cache_json = WorkWithJson.read_data(path_json)
        for vacancy_with_cache_json in cache_json:
            if vacancy_with_cache_json['unique'] in del_list:
                continue
            else:
                vacancy = HhruVacancy(
                    name=vacancy_with_cache_json['name'],
                    url=vacancy_with_cache_json['url'],
                    description=vacancy_with_cache_json['description'],
                    salary=vacancy_with_cache_json['salary'],
                    city=vacancy_with_cache_json['city']
                )
                vacancies.append(vacancy.save_data_about_vacancy(unique))
                unique += 1
        cls.save_data_vacancies(path_json_del_result, vacancies)

    @classmethod
    def cut_n_vacancies(cls, cut_list: list, path_json: str, path_json_cut_result: str) -> None:
        """Cut n vacancies by list in which the vacancies numbers are transmitted"""

        unique = 1
        vacancies: list = []
        cache_json = WorkWithJson.read_data(path_json)
        for vacancy_with_cache_json in cache_json:
            if vacancy_with_cache_json['unique'] in cut_list:
                vacancy = HhruVacancy(
                    name=vacancy_with_cache_json['name'],
                    url=vacancy_with_cache_json['url'],
                    description=vacancy_with_cache_json['description'],
                    salary=vacancy_with_cache_json['salary'],
                    city=vacancy_with_cache_json['city']
                )
                vacancies.append(vacancy.save_data_about_vacancy(unique))
                unique += 1
        cls.save_data_vacancies(path_json_cut_result, vacancies)
