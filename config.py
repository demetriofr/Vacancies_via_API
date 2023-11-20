from pathlib import Path


class ConfigForHhru:
    """Config for hh.ru"""

    URL_HHRU = 'https://api.hh.ru/vacancies'
    JSON_HHRU = Path(Path(__file__).parent, 'cache', 'cache_hhru.json')

    AREA = 113  # Country ID (default 113 - Russia)
    PAGE = 0  # Search result page number (default = 0)
    PER_PAGE = 15  # Number of results per search page


class ConfigForSjru:
    """Config for superjob.ru"""

    URL_SJRU = 'https://api.superjob.ru/2.0/vacancies/'
    JSON_SJRU = Path(Path(__file__).parent, 'cache', 'cache_sjru.json')

    # Default for superjob.ru
    COUNTRY = {'id_country': 1},  # Country ID (default 1 - Russia)
    PAGE = 0  # Search result page number (default = 0)
    COUNT = 15  # Number of results per search page

