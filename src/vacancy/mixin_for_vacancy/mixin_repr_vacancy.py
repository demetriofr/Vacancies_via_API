from text import REPR_VACANCY


class ReprVacancy:
    """Displays information about the vacancy."""

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

    def __repr__(self):
        return REPR_VACANCY.format(name=self.name,
                                   url=self.url,
                                   description=self.description,
                                   salary=self.salary,
                                   city=self.city
                                   )
