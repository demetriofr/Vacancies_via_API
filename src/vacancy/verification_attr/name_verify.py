class NameVerify:
    """Verification the name attribute of the Vacancy class."""

    def __init__(self, name):
        self.name = name

    @classmethod
    def verify_name(cls, name):
        if isinstance(name, str):
            return name
        else:
            return ' - '

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        name = self.verify_name(name)
        self.__name = name
