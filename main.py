from pprint import pprint as pp

from src.api_work.hhru_api import HhruApi
from src.api_work.sjru_api import SjruApi

if __name__ == '__main__':
    # hhru = HhruApi('python')
    # pp(hhru.get_data_api())
    sjru = SjruApi('python')
    pp(sjru.get_data_api())
