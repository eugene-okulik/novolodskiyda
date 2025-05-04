import pytest


@pytest.fixture(scope="session")
def session_scope():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture()
def function_scope():
    print("before test")
    yield
    print("after test")
