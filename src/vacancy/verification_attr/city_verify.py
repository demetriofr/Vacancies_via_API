class CityVerify:
    """Verification the city attribute of the Vacancy class"""

    def __init__(self, city):
        self.city = city

    @classmethod
    def verify_city(cls, city):
        if isinstance(city, str):
            return city
        else:
            return ' - '

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        city = self.verify_city(city)
        self.__city = city
