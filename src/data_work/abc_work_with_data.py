from abc import ABC, abstractmethod


class WorkWithData(ABC):
    """Abstract class for working with the data."""

    @classmethod
    @abstractmethod
    def clear_data(cls, data):
        pass

    @classmethod
    def save_data(cls, path, data):
        pass

    @classmethod
    def read_data(cls, path):
        pass
