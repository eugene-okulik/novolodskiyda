import pytest
from test_api_project.endpoints.object.delete_object import DeleteObject
from test_api_project.endpoints.object.get_objects import GetObjects
from test_api_project.endpoints.object.get_object_id import GetObjectId
from test_api_project.endpoints.object.patch_object import PatchObject
from test_api_project.endpoints.object.post_object import PostObject
from test_api_project.endpoints.object.put_object import PutObject
from test_api_project.tests.test_data.generate_test_data import generate_test_data


@pytest.fixture()
def create_get_objects_endpoint():
    return GetObjects()


@pytest.fixture()
def create_get_object_id_endpoint():
    return GetObjectId()


@pytest.fixture()
def create_post_object_endpoint():
    return PostObject()


@pytest.fixture()
def create_put_object_endpoint():
    return PutObject()


@pytest.fixture()
def create_patch_object_endpoint():
    return PatchObject()


@pytest.fixture()
def create_delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def create_and_delete(create_post_object_endpoint, create_delete_object_endpoint):
    create_post_object_endpoint.post_object(generate_test_data())
    object_id = create_post_object_endpoint.response.json()['id']
    yield object_id
    create_delete_object_endpoint.delete_object_id(object_id=object_id)


@pytest.fixture()
def create_object(create_post_object_endpoint):
    create_post_object_endpoint.post_object(generate_test_data())
    return create_post_object_endpoint.response.json()['id']


@pytest.fixture()
def delete_after_test(create_delete_object_endpoint):
    delete_after_test = create_delete_object_endpoint
    delete_after_test.object_id = None
    yield delete_after_test
    if delete_after_test.object_id:
        delete_after_test.delete_object_id(object_id=delete_after_test.object_id)
