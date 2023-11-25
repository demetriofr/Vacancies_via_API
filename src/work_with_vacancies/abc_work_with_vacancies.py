from abc import ABC, abstractmethod


class WorkWithVacancies(ABC):
    """Abstract class for work with vacancies."""

    @classmethod
    @abstractmethod
    def get_data_about_vacancies(cls):
        pass
