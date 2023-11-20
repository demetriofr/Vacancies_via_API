from src.api_work.sjru_api import SjruApi


def test_sjru_api():
    sjru_api = SjruApi('python')

    assert str(sjru_api.connect_to_api()) == '<Response [200]>'
    assert type(sjru_api.get_data_api()) == dict
    assert sjru_api.save_data_api() is None