from abc import ABC, abstractmethod


class WorkWithVacancy(ABC):
    """Abstract class for working with the vacancy."""

    @abstractmethod
    def __init__(self,
                 name: str,
                 url: str,
                 description: str,
                 salary: int | dict | None,
                 city: str
                 ):
        pass
