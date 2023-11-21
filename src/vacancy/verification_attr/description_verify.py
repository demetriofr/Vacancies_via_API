class DescriptionVerify:
    """Verification the description attribute of the Vacancy class"""

    def __init__(self, description):
        self.description = description

    @classmethod
    def verify_description(cls, description):
        if isinstance(description, str):
            return description
        else:
            return ' - '

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        description = self.verify_description(description)
        self.__description = description
