import pytest


@pytest.fixture()
def dataLoad():
    print("Data profile details:")
    return ["Anjali", "Bhat", "anjali@gamil.com"]

@pytest.fixture()
def setup():
    print("I will be executed first")
    yield
    print("I will be executed last")