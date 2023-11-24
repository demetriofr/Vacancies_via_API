from config import ConfigForHhru
from src.data_work.work_with_json import WorkWithJson
from src.vacancy.hhru_vacancy import HhruVacancy
from src.work_with_vacancies.abc_work_with_vacancies import WorkWithVacancies
from src.work_with_vacancies.mixin_for_vacancies.mixin_delete_cut_n_vacancies import DeleteCutNVacancies
from src.work_with_vacancies.mixin_for_vacancies.mixin_print_data_vacancies import PrintDataVacancies


class WorkWithVacanciesHhru(WorkWithVacancies, DeleteCutNVacancies, PrintDataVacancies):
    """Work with vacancies with hh.ru saved in JSON"""

    @classmethod
    def get_data_about_vacancies(cls):
        """Get and use data about vacancies by Vacancy class"""
        unique = 1
        vacancies: list = []
        cache_api = WorkWithJson.read_data(ConfigForHhru.JSON_HHRU)
        for vacancy_with_cache_api in cache_api:
            vacancy = HhruVacancy(
                name=vacancy_with_cache_api['name'],
                url=vacancy_with_cache_api['alternate_url'],
                description=vacancy_with_cache_api['snippet']['responsibility'],
                salary=vacancy_with_cache_api['salary'],
                city=vacancy_with_cache_api['area']['name']
            )
            vacancies.append(vacancy.save_data_about_vacancy(unique))
            unique += 1
        cls.save_data_vacancies(ConfigForHhru.JSON_HHRU_VACANCY, vacancies)
