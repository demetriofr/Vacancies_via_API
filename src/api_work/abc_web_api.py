from abc import ABC, abstractmethod


class WorkWithWebApi(ABC):
    """Abstract class for working with the API"""

    @abstractmethod
    def connect_to_api(self):
        pass

    def get_data_api(self):
        pass

    def save_data_api(self):
        pass
