import requests
from faker import Faker
import pytest
import allure

fake = Faker()


@pytest.mark.critical
@pytest.mark.parametrize("name,color,country", [
    ('jon', 'red', 'rus'),
    ('smit', 'grey', 'kz'),
    ('luisa', 'brown', 'eu')
])
@allure.feature('Post')
@allure.story('Munipulet with posts')
@allure.title('Создание нового поста')
def test_post_object(name, color, country, function_scope):
    body = {
        "name": f"{name}",
        "data": {"color": f"{color}", "country": f"{country}"}
    }
    headers = {'Content-Type': 'application/json'}
    with allure.step('Run post new object'):
        response = requests.post(
            'http://167.172.172.115:52353/object',
            json=body,
            headers=headers
        )
    object_id = response.json()['id']
    with allure.step('Check that status cod 200'):
        assert response.status_code < 300, 'Status code is incorrect'
    assert response.json()['name'] == name, 'Name is incorrect'
    assert response.json()['data']['color'] == color, 'Color is incorrect'
    assert response.json()['data']['country'] == country, 'Country is incorrect'
    requests.delete(f'http://167.172.172.115:52353/object/{object_id}')


@pytest.mark.medium
@allure.feature('Put')
@allure.story('Munipulet with posts')
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


@allure.feature('Patch')
@allure.story('Munipulet with posts')
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


@allure.feature('Delete')
@allure.story('Munipulet with posts')
def test_delete_a_object(object_for_test, function_scope):
    object_id = object_for_test
    response = requests.delete(f'http://167.172.172.115:52353/object/{object_id}')
    assert response.status_code < 300, 'Status code is incorrect'
