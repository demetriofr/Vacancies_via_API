from config import ConfigForHhru, ConfigForSjru
from src.api_work.hhru_api import HhruApi
from src.api_work.sjru_api import SjruApi
from src.data_work.work_with_json import WorkWithJson
from src.interface.interface_console import InterfaceConsole
from src.work_with_vacancies.work_with_vacancies_hhru import WorkWithVacanciesHhru
from src.work_with_vacancies.work_with_vacancies_sjru import WorkWithVacanciesSjru
from text import FINAL_PRINT


class MainConsole(InterfaceConsole):
    """Main console for work with interface."""

    @classmethod
    def main_console(cls):
        """Main console for work."""

        exit_app = 1

        while exit_app == 1:
            site = cls.site_and_keyword()
            if site == 1:
                cls.del_or_cut_vacancies_hhru()
            else:
                cls.del_or_cut_vacancies_sjru()
            if cls.go_on() == 1:
                continue
            else:
                exit_app = 0

            print(FINAL_PRINT)

    @classmethod
    def site_and_keyword(cls):
        """Choose the site to get the API and search for the keyword."""

        site = None

        while site not in [0, 1, 2]:
            site = int(cls.choosing_site_for_search())  # 1 - hh.ru, 2 - superjob.ru
            key_word = cls.input_keyword()

            if site == 1:
                hhru = HhruApi(key_word)
                path_json_vacancies = ConfigForHhru.JSON_HHRU_VACANCY
                hhru.get_data_api()
                hhru.save_data_api()
                WorkWithVacanciesHhru.get_data_about_vacancies()
                WorkWithVacanciesHhru.print_data_vacancies(path_json_vacancies)

            elif site == 2:
                sjru = SjruApi(key_word)
                path_json_vacancies = ConfigForSjru.JSON_SJRU_VACANCY
                sjru.get_data_api()
                sjru.save_data_api()
                WorkWithVacanciesSjru.get_data_about_vacancies()
                WorkWithVacanciesSjru.print_data_vacancies(path_json_vacancies)

            else:
                continue

            return site

    @classmethod
    def del_or_cut_vacancies_hhru(cls):
        """Delete or cut vacancies from list."""

        path_json_vacancy = ConfigForHhru.JSON_HHRU_VACANCY
        path_json_vacancy_del_result = ConfigForHhru.JSON_HHRU_VACANCY_DEL_RESULT
        path_json_vacancy_cut_result = ConfigForHhru.JSON_HHRU_VACANCY_CUT_RESULT

        del_or_cut_vacancies = None

        while del_or_cut_vacancies not in [0, 1, 2]:
            del_or_cut_vacancies = cls.input_del_or_del_vacancies()  # 1 - delete, 2 - cut

            if del_or_cut_vacancies == 1:

                del_list = cls.check_list_for_del_or_cut(cls.get_list_for_del(), path_json_vacancy)

                if del_list is False:
                    del_or_cut_vacancies = None
                    continue
                else:
                    WorkWithVacanciesHhru.delete_n_vacancies(
                        del_list,
                        path_json_vacancy,
                        path_json_vacancy_del_result
                    )
                    WorkWithVacanciesHhru.print_data_vacancies(path_json_vacancy_del_result)

            elif del_or_cut_vacancies == 2:

                cut_list = cls.check_list_for_del_or_cut(cls.get_list_for_cut(), path_json_vacancy)

                if cut_list is False:
                    del_or_cut_vacancies = None
                    continue
                else:
                    WorkWithVacanciesHhru.cut_n_vacancies(
                        cut_list,
                        path_json_vacancy,
                        path_json_vacancy_cut_result
                    )
                    WorkWithVacanciesHhru.print_data_vacancies(path_json_vacancy_cut_result)

            elif del_or_cut_vacancies == 0:
                del_or_cut_vacancies = 0

            else:
                del_or_cut_vacancies = None

    @classmethod
    def del_or_cut_vacancies_sjru(cls):
        """Delete or cut vacancies from list."""

        path_json_vacancy = ConfigForSjru.JSON_SJRU_VACANCY
        path_json_vacancy_result = ConfigForSjru.JSON_SJRU_VACANCY_DEL_RESULT
        path_json_vacancy_cut_result = ConfigForSjru.JSON_SJRU_VACANCY_CUT_RESULT

        del_or_cut_vacancies = None

        while del_or_cut_vacancies not in [0, 1, 2]:
            del_or_cut_vacancies = cls.input_del_or_del_vacancies()  # 1 - delete, 2 - cut
            if del_or_cut_vacancies == 1:

                del_list = cls.check_list_for_del_or_cut(cls.get_list_for_del(), path_json_vacancy)

                if del_list is False:
                    del_or_cut_vacancies = None
                    continue
                else:
                    WorkWithVacanciesSjru.delete_n_vacancies(
                        del_list,
                        path_json_vacancy,
                        path_json_vacancy_result
                    )
                    WorkWithVacanciesSjru.print_data_vacancies(path_json_vacancy_result)

            elif del_or_cut_vacancies == 2:

                cut_list = cls.check_list_for_del_or_cut(cls.get_list_for_cut(), path_json_vacancy)

                if cut_list is False:
                    del_or_cut_vacancies = None
                    continue
                else:
                    WorkWithVacanciesSjru.cut_n_vacancies(
                        cut_list,
                        path_json_vacancy,
                        path_json_vacancy_cut_result
                    )
                    WorkWithVacanciesSjru.print_data_vacancies(path_json_vacancy_cut_result)

            elif del_or_cut_vacancies == 0:
                del_or_cut_vacancies = 0

            else:
                del_or_cut_vacancies = None

    @staticmethod
    def check_list_for_del_or_cut(list_for_check, path_json):
        """Check the list that contains vacancy numbers to see if those numbers are in the vacancies lists."""

        try:
            list_of_numbers_vacancies = [key_['unique'] for key_ in WorkWithJson.read_data(path_json)]

            if all(i in tuple(list_of_numbers_vacancies) for i in tuple(list_for_check)):
                return list_for_check
            else:
                return False
        except ValueError:
            return False
