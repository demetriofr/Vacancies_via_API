from src.vacancy.verification_attr.city_verify import CityVerify
from src.vacancy.verification_attr.description_verify import DescriptionVerify
from src.vacancy.verification_attr.name_verify import NameVerify
from src.vacancy.verification_attr.salary_verify import SalaryVerify
from src.vacancy.verification_attr.url_verify import UrlVerify


class AttrVerify(
    NameVerify,
    UrlVerify,
    DescriptionVerify,
    SalaryVerify,
    CityVerify
):
    pass
