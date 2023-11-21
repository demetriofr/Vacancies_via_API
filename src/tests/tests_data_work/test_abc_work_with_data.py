import pytest

from src.data_work.abc_work_with_data import WorkWithData


@pytest.mark.xfail(raises=TypeError)
def test_abc_web_api():
    work_data = WorkWithData()
    return work_data
