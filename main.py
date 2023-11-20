from pprint import pprint as pp

from src.api_work.hhru_api import HhruApi

if __name__ == '__main__':
    hhru = HhruApi('python')
    pp(hhru.get_data_api())
