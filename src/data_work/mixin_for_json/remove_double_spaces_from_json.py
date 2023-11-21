class RemoveDoubleSpacesFromJson:
    """Remove double spaces from complex JSON"""

    @classmethod
    def remove_double_spaces(cls, data):
        """Remove double spaces"""

        if isinstance(data, str):
            return ' '.join(data.split())
        elif isinstance(data, list):
            return [cls.remove_double_spaces(item) for item in data]
        elif isinstance(data, dict):
            return {key: cls.remove_double_spaces(value) for key, value in data.items()}
        else:
            return data
