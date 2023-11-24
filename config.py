from pathlib import Path


class ConfigForHhru:
    """Config for hh.ru"""

    URL_HHRU = 'https://api.hh.ru/vacancies'
    JSON_HHRU = Path(Path(__file__).parent, 'cache', 'cache_hhru.json')
    JSON_HHRU_VACANCY = Path(Path(__file__).parent, 'cache', 'cache_hhru_vacancy.json')
    JSON_HHRU_VACANCY_DEL_RESULT = Path(Path(__file__).parent, 'cache', 'cache_hhru_vacancy_del_result.json')
    JSON_HHRU_VACANCY_CUT_RESULT = Path(Path(__file__).parent, 'cache', 'cache_hhru_vacancy_cut_result.json')

    AREA = 113  # Country ID (default 113 - Russia)
    PAGE = 0  # Search result page number (default = 0)
    PER_PAGE = 15  # Number of results per search page


class ConfigForSjru:
    """Config for superjob.ru"""

    URL_SJRU = 'https://api.superjob.ru/2.0/vacancies/'
    JSON_SJRU = Path(Path(__file__).parent, 'cache', 'cache_sjru.json')
    JSON_SJRU_VACANCY = Path(Path(__file__).parent, 'cache', 'cache_sjru_vacancy.json')
    JSON_SJRU_VACANCY_DEL_RESULT = Path(Path(__file__).parent, 'cache', 'cache_sjru_vacancy_del_result.json')
    JSON_SJRU_VACANCY_CUT_RESULT = Path(Path(__file__).parent, 'cache', 'cache_sjru_vacancy_cut_result.json')

    # Default for superjob.ru
    COUNTRY = {'id_country': 1},  # Country ID (default 1 - Russia)
    PAGE = 0  # Search result page number (default = 0)
    COUNT = 15  # Number of results per search page
