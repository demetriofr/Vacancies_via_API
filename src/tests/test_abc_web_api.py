import pytest

from src.api_work.abc_web_api import WorkWithWebApi


@pytest.mark.xfail(raises=TypeError)
def test_abc_web_api():
    work_api = WorkWithWebApi()
