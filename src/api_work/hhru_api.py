import requests

from config import URL_HHRU, VACANCY_SEARCH_FIELD, AREA, PAGE, PAGES, PER_PAGE
from src.api_work.abc_web_api import WorkWithWebApi


class HhruApi(WorkWithWebApi):
    """Work with API hh.ru"""

    def __init__(self,
                 text: str,
                 vacancy_search_field: list = VACANCY_SEARCH_FIELD,
                 area: int = AREA,
                 page: int = PAGE,
                 pages: int = PAGES,
                 per_page: int = PER_PAGE
                 ):
        self.url = URL_HHRU
        self.text = text
        self.vacancy_search_field = vacancy_search_field
        self.per_page = per_page
        self.area = area
        self.page = page
        self.pages = pages
        self.parameter: dict = {'text': self.text,
                                'vacancy_search_field': self.vacancy_search_field,
                                'per_page': self.per_page,
                                'page': self.page,
                                'pages': self.pages,
                                'area': self.area
                                }

    def connect_to_api(self):
        """Connect to API hh.ru"""
        response = requests.get(self.url, self.parameter)
        return response

    def get_data_api(self):
        """Get data with API hh.ru"""
        return self.connect_to_api().json()

    def save_data_api(self):
        """Save data with API hh.ru"""
        pass
