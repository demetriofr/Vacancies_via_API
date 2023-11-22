import requests

from config import ConfigForHhru
from src.api_work.abc_web_api import WorkWithWebApi
from src.data_work.work_with_json import WorkWithJson


class HhruApi(WorkWithWebApi):
    """Work with API hh.ru"""

    def __init__(self,
                 text: str,
                 area: int = ConfigForHhru.AREA,
                 page: int = ConfigForHhru.PAGE,
                 per_page: int = ConfigForHhru.PER_PAGE
                 ):
        self.url = ConfigForHhru.URL_HHRU
        self.parameter: dict = {'text': text,
                                'area': area,
                                'per_page': per_page,
                                'page': page
                                }

    def connect_to_api(self):
        """Connect to API hh.ru"""
        response = requests.get(self.url, self.parameter)
        return response

    def get_data_api(self):
        """Get data with API hh.ru"""
        return self.connect_to_api().json()["items"]

    def save_data_api(self):
        """Save data with API hh.ru"""
        return WorkWithJson.save_data(ConfigForHhru.JSON_HHRU, self.get_data_api())
