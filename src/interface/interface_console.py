from text import CHOOSING_SITE, KEYWORD_FOR_SEARCH


class InterfaceConsole:
    """For search vacancy using the console"""

    @classmethod
    def choosing_site_for_search(cls):
        """Choosing a site for search for vacancies"""
        return input(CHOOSING_SITE)

    @classmethod
    def input_keyword(cls):
        """Enter your search term"""
        return input(KEYWORD_FOR_SEARCH)

