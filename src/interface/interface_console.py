from text import CHOOSING_SITE, KEYWORD_FOR_SEARCH, DEL_OR_CUT_VACANCIES, DEL_LIST, CUT_LIST, GO_ON


class InterfaceConsole:
    """For search vacancy using the console"""

    @classmethod
    def choosing_site_for_search(cls):
        """Choosing a site for search for vacancies"""
        try:
            choosing_site = int(input(CHOOSING_SITE))
        except ValueError:
            choosing_site = 100
        return choosing_site

    @classmethod
    def input_keyword(cls):
        """Enter your search term"""
        return input(KEYWORD_FOR_SEARCH)

    @classmethod
    def input_del_or_del_vacancies(cls):
        """Enter for delete or cut vacancies"""
        try:
            del_or_del_vacancies = int(input(DEL_OR_CUT_VACANCIES))
        except ValueError:
            del_or_del_vacancies = 100
        return del_or_del_vacancies

    @classmethod
    def get_list_for_del(cls):
        """Get list for delete vacancies"""
        try:
            choosing_site = cls.create_list_from_str(input(DEL_LIST))
        except ValueError:
            choosing_site = 100
        return choosing_site

    @classmethod
    def get_list_for_cut(cls):
        """Get list for cut vacancies"""
        try:
            choosing_site = cls.create_list_from_str(input(CUT_LIST))
        except ValueError:
            choosing_site = 100
        return choosing_site

    @classmethod
    def go_on(cls):
        """Continue working with vacancies"""
        try:
            go_on_ = int(input(GO_ON))
        except ValueError:
            go_on_ = 100
        return go_on_

    @staticmethod
    def create_list_from_str(str_input):
        """Create list from string"""
        try:
            list_input = [int(str_input_) for str_input_ in str_input.split(' ')]
        except ValueError:
            list_input = False
        return list_input

