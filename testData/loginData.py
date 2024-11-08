import pytest


@pytest.fixture(params=[{"username": 999, "password": 1}])
def getSuperAdminLoginData(request):
    return request.param
