import requests
from faker import Faker
import allure

fake = Faker()


@allure.feature('Get')
@allure.story('Looking post')
def test_get_objects(session_scope, function_scope):
    response = requests.get('http://167.172.172.115:52353/object')
    assert response.status_code < 300, 'Status code is incorrect'
    assert response.json() != {}, 'Objects not found'


@allure.feature('Get')
@allure.story('Looking post')
def test_get_object_id(object_for_test, function_scope):
    object_id = object_for_test
    response = requests.get(f'http://167.172.172.115:52353/object/{object_id}')
    assert response.status_code < 300, 'Status code is incorrect'
