from pathlib import Path

# For hh.ru
URL_HHRU = 'https://api.hh.ru/vacancies'
JSON_HHRU = Path(Path(__file__).parent, 'cache', 'cache_hhru.json')

# Default for hh.ru
VACANCY_SEARCH_FIELD = [
    'name',
    'description'
]
AREA = 113
PAGE = 0
PAGES = 50
PER_PAGE = 10
