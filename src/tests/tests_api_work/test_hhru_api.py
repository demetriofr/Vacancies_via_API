from src.api_work.hhru_api import HhruApi


def test_hhru_api():
    hhru_api = HhruApi('python')

    assert str(hhru_api.connect_to_api()) == '<Response [200]>'
    assert type(hhru_api.get_data_api()) == dict
    assert hhru_api.save_data_api() is None
