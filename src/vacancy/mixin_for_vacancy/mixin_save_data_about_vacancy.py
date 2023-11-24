class SaveDataAboutVacancy:
    """Save data about vacancy in dictionary"""

    def __init__(self,
                 name: str,
                 url: str,
                 description: str,
                 salary: int | dict | None,
                 city: str
                 ):
        self.name = name
        self.url = url
        self.description = description
        self.salary = salary
        self.city = city

    def save_data_about_vacancy(self, unique: int) -> dict:
        """Save data about vacancy"""

        vacancy_n = {
            'unique': unique,
            'name': self.name,
            'url': self.url,
            'description': self.description,
            'salary': self.salary,
            'city': self.city
        }
        return vacancy_n
