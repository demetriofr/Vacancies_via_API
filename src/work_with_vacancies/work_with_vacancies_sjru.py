from config import ConfigForSjru
from src.data_work.work_with_json import WorkWithJson
from src.vacancy.sjru_vacancy import SjruVacancy
from src.work_with_vacancies.abc_work_with_vacancies import WorkWithVacancies
from src.work_with_vacancies.mixin_for_vacancies.mixin_delete_cut_n_vacancies import DeleteCutNVacancies
from src.work_with_vacancies.mixin_for_vacancies.mixin_print_data_vacancies import PrintDataVacancies


class WorkWithVacanciesSjru(WorkWithVacancies, DeleteCutNVacancies, PrintDataVacancies):
    """Work with vacancies with superjob.ru saved in JSON."""

    @classmethod
    def get_data_about_vacancies(cls):
        """Get and use data about vacancies by Vacancy class."""
        unique = 1
        vacancies: list = []
        cache_api = WorkWithJson.read_data(ConfigForSjru.JSON_SJRU)
        for vacancy_with_cache_api in cache_api:
            vacancy = SjruVacancy(
                name=vacancy_with_cache_api['profession'],
                url=vacancy_with_cache_api['link'],
                description=vacancy_with_cache_api['candidat'],
                salary=vacancy_with_cache_api['payment_from'],
                city=vacancy_with_cache_api['town']['title']
            )
            vacancies.append(vacancy.save_data_about_vacancy(unique))
            unique += 1
        cls.save_data_vacancies(ConfigForSjru.JSON_SJRU_VACANCY, vacancies)
