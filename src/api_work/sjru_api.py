import os

import requests
from dotenv import load_dotenv

from config import ConfigForSjru
from src.api_work.abc_web_api import WorkWithWebApi
from src.data_work.work_with_json import WorkWithJson


class SjruApi(WorkWithWebApi):
    """Work with API superjob.ru."""

    load_dotenv()
    X_Api_App_Id = os.getenv('SECRET_KEY_SUPERJOB')

    def __init__(self,
                 text: str,
                 area: dict = ConfigForSjru.COUNTRY,
                 page: int = ConfigForSjru.PAGE,
                 per_page: int = ConfigForSjru.COUNT
                 ):
        self.url = ConfigForSjru.URL_SJRU
        self.parameter: dict = {'keyword': text,
                                'town': area,
                                'page': page,
                                'count': per_page
                                }

    def connect_to_api(self):
        """Connect to API superjob.ru."""

        headers = {"X-Api-App-Id": self.X_Api_App_Id}
        response = requests.get(self.url, params=self.parameter, headers=headers)
        return response

    def get_data_api(self):
        """Get data with API superjob.ru."""
        return self.connect_to_api().json()["objects"]

    def save_data_api(self):
        """Save data with API superjob.ru."""
        return WorkWithJson.save_data(ConfigForSjru.JSON_SJRU, self.get_data_api())
