import requests
from faker import Faker
import pytest

fake = Faker()


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


def test_get_objects(session_scope, function_scope):
    response = requests.get('http://167.172.172.115:52353/object')
    assert response.status_code < 300, 'Status code is incorrect'
    assert response.json() != {}, 'Objects not found'


def test_get_object_id(object_for_test, function_scope):
    object_id = object_for_test
    response = requests.get(f'http://167.172.172.115:52353/object/{object_id}')
    assert response.status_code < 300, 'Status code is incorrect'


@pytest.mark.critical
@pytest.mark.parametrize("name,color,country", [
    (fake.name(), fake.color(), fake.country()),
    (fake.name(), fake.color(), fake.country()),
    (fake.name(), fake.color(), fake.country())
])
def test_post_object(name, color, country, function_scope):
    body = {
        "name": f"{name}",
        "data": {"color": f"{color}", "country": f"{country}"}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    object_id = response.json()['id']
    assert response.status_code < 300, 'Status code is incorrect'
    assert response.json()['name'] == name, 'Name is incorrect'
    assert response.json()['data']['color'] == color, 'Color is incorrect'
    assert response.json()['data']['country'] == country, 'Country is incorrect'
    requests.delete(f'http://167.172.172.115:52353/object/{object_id}')


@pytest.mark.medium
def test_put_a_object(object_for_test, function_scope):
    object_id = object_for_test
    name = fake.name()
    color = fake.color()
    country = fake.country()
    body = {
        "name": f"{name}",
        "data": {"color": f"{color}", "country": f"{country}"}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://167.172.172.115:52353/object/{object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code < 300, 'Status code is incorrect'
    assert response.json()['name'] == name, 'Name is incorrect'
    assert response.json()['data']['color'] == color, 'Color is incorrect'
    assert response.json()['data']['country'] == country, 'Country is incorrect'


def test_patch_a_object(object_for_test, function_scope):
    object_id = object_for_test
    name = fake.name()
    body = {
        "name": f"{name}"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://167.172.172.115:52353/object/{object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code < 300, 'Status code is incorrect'
    assert response.json()['name'] == name, 'Name is incorrect'


def test_delete_a_object(object_for_test, function_scope):
    object_id = object_for_test
    response = requests.delete(f'http://167.172.172.115:52353/object/{object_id}')
    assert response.status_code < 300, 'Status code is incorrect'
