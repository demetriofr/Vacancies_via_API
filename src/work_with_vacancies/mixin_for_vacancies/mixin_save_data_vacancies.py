from src.data_work.work_with_json import WorkWithJson


class SaveDataVacancies:
    """Save data about vacancies by Vacancy class"""

    @classmethod
    def save_data_vacancies(cls, path_json, vacancies):
        """Save data about vacancies"""
        return WorkWithJson.save_data(path_json, vacancies)
