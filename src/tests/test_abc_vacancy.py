import pytest

from src.vacancy.abc_vacancy import WorkWithVacancy


@pytest.mark.xfail(raises=TypeError)
def test_abc_vacancy():
    work_vacancy = WorkWithVacancy()
    return work_vacancy
