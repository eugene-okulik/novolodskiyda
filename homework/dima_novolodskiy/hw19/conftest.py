import pytest
import requests
from faker import Faker

fake = Faker()


@pytest.fixture()
def object_for_test():
    body = {
        "name": f"{fake.name()}",
        "data": {"color": f"{fake.color()}", "country": f"{fake.country()}"}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    object_id = response.json()['id']
    yield object_id
    requests.delete(f'http://167.172.172.115:52353/object/{object_id}')


@pytest.fixture(scope="session")
def session_scope():
    print("Start testing")
    yield
    print("Testing completed")


# Function-scoped fixture for before/after each test
@pytest.fixture()
def function_scope():
    print("before test")
    yield
    print("after test")
