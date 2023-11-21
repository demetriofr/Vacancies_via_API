import os

from src.api_work.hhru_api import HhruApi
from src.data_work.work_with_json import WorkWithJson


def test_work_with_json():
    hhru_api = HhruApi('python')
    data_api = hhru_api.get_data_api()

    assert type(WorkWithJson.clear_data(data_api)) == dict
    assert WorkWithJson.save_data('tmp_api.json', data_api) is None
    assert type(WorkWithJson.read_data('tmp_api.json',)) == dict
    os.remove('tmp_api.json')
