import requests
from faker import Faker

fake = Faker()


def get_objects():
    response = requests.get(f'http://167.172.172.115:52353/object')
    assert response.status_code < 300, 'Status code is incorrect'
    assert response.json() != {}, 'Objects not found'
    print("Passed 'get_objects'")


def get_object_id():
    object_id = new_object()
    response = requests.get(f'http://167.172.172.115:52353/object/{object_id}')
    assert response.status_code < 300, 'Status code is incorrect'
    clear_object(object_id)
    print("Passed 'get_object_id'")


def new_object():
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
    print(f"Add new object: {response.json()['id']}")
    return response.json()['id']


def post_object():
    name = fake.name()
    color = fake.color()
    country = fake.country()
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
    assert response.status_code < 300, 'Status code is incorrect'
    assert response.json()['name'] == name, 'Name is incorrect'
    assert response.json()['data']['color'] == color, 'Color is incorrect'
    assert response.json()['data']['country'] == country, 'Country is incorrect'
    clear_object(response.json()['id'])
    print("Passed 'post_object'")


def put_a_object():
    object_id = new_object()
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
    clear_object(object_id)
    print("Passed 'put_a_object'")


def patch_a_object():
    object_id = new_object()
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
    clear_object(object_id)
    print("Passed 'patch_a_object'")


def delete_a_object():
    object_id = new_object()
    response = requests.delete(f'http://167.172.172.115:52353/object/{object_id}')
    assert response.status_code < 300, 'Status code is incorrect'
    print("Passed 'delete_a_object'")


def clear_object(object_id):
    requests.delete(f'http://167.172.172.115:52353/object/{object_id}')
    print(f'Remove object: {object_id}')


get_objects()
get_object_id()
post_object()
put_a_object()
patch_a_object()
delete_a_object()
