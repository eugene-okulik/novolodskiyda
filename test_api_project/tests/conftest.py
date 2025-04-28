from faker import Faker
import pytest

from test_api_project.endpoints.object.delete_object import DeleteObject
from test_api_project.endpoints.object.get_objects import GetObjects
from test_api_project.endpoints.object.get_object_id import GetObjectId
from test_api_project.endpoints.object.patch_object import PatchObject
from test_api_project.endpoints.object.post_object import PostObject
from test_api_project.endpoints.object.put_object import PutObject

fake = Faker()


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
def generated_post_data():
    return {
        "name": fake.name(),
        "data": {
            "color": fake.color(),
            "country": fake.country()
        }
    }


@pytest.fixture()
def generated_put_data():
    return {
        "name": fake.name(),
        "data": {
            "color": fake.color(),
            "country": fake.country()
        }
    }
