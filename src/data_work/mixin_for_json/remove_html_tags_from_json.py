import re


class RemoveHtmlTagsFromJson:
    """Remove html tags from complex JSON"""

    @classmethod
    def remove_html_tags_re(cls, data):
        """Remove html tags with re"""

        if isinstance(data, str):
            return re.sub(re.compile('<.*?>'), ' ', data)
        elif isinstance(data, list):
            return [cls.remove_html_tags_re(item) for item in data]
        elif isinstance(data, dict):
            return {key: cls.remove_html_tags_re(value) for key, value in data.items()}
        else:
            return data
