from json import dump, load

from src.data_work.abc_work_with_data import WorkWithData
from src.data_work.mixin_for_json.remove_double_spaces_from_json import RemoveDoubleSpacesFromJson
from src.data_work.mixin_for_json.remove_html_tags_from_json import RemoveHtmlTagsFromJson


class WorkWithJson(WorkWithData, RemoveDoubleSpacesFromJson, RemoveHtmlTagsFromJson):
    """Work with JSON"""

    @classmethod
    def clear_data(cls, data):
        """Clear JSON from html tags and double spaces"""
        data = cls.remove_html_tags_re(data)
        data = cls.remove_double_spaces(data)
        return data

    @classmethod
    def save_data(cls, path, data):
        """Save JSON to a file"""
        with open(path, 'w', encoding='utf-8') as f:
            data = cls.clear_data(data)
            dump(data, f, ensure_ascii=False, indent=4)

    @classmethod
    def read_data(cls, path):
        """Read JSON from a file"""
        with open(path, 'r', encoding='utf-8') as f:
            return load(f)
