from abc import ABC, abstractmethod


class WorkWithVacancy(ABC):
    """Abstract class for working with the vacancy"""

    @abstractmethod
    def get_data_about_vacancy(self, vacancy):
        pass
