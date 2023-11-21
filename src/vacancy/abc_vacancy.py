from abc import ABC, abstractmethod


class WorkWithVacancy(ABC):
    """Abstract class for working with the vacancy"""

    @abstractmethod
    def __lt__(self, other):
        """For comparison 'less'"""
        pass

    def __gt__(self, other):
        """For comparison 'more'"""
        pass

    def __le__(self, other):
        """For comparison 'less or equal'"""
        pass

    def __ge__(self, other):
        """For comparison 'more or equal'"""
        pass

    def __eq__(self, other):
        """For comparison 'equal'"""
        pass

    def __ne__(self, other):
        """For comparison 'unequal'"""
        pass
