from test_api_project.tests.test_data.generate_test_data import generate_test_data


def test_get_objects(create_get_objects_endpoint):
    create_get_objects_endpoint.get_all_objects()
    create_get_objects_endpoint.check_objects_in_response()
    create_get_objects_endpoint.check_status_code_200()


def test_get_object_id(create_get_object_id_endpoint, create_and_delete):
    create_get_object_id_endpoint.get_object_id(create_and_delete)
    create_get_object_id_endpoint.check_status_code_200()
    create_get_object_id_endpoint.check_name(name=create_get_object_id_endpoint.response.json()['name'])


def test_post_object(
        create_post_object_endpoint,
        create_get_object_id_endpoint,
        delete_after_test
):
    test_data = generate_test_data()
    create_post_object_endpoint.post_object(test_data)
    create_post_object_endpoint.check_status_code_200()
    create_post_object_endpoint.check_name_in_response(test_data['name'])
    create_get_object_id_endpoint.get_object_id(create_post_object_endpoint.response.json()['id'])
    create_get_object_id_endpoint.check_name(create_post_object_endpoint.response.json()['name'])
    delete_after_test.object_id = create_post_object_endpoint.response.json()['id']


def test_put_a_object(
        create_put_object_endpoint,
        create_get_object_id_endpoint,
        create_and_delete
):
    test_data = generate_test_data()
    create_put_object_endpoint.put_object(payload=test_data, object_id=create_and_delete)
    create_put_object_endpoint.check_status_code_200()
    create_get_object_id_endpoint.get_object_id(create_and_delete)
    create_get_object_id_endpoint.check_name(create_put_object_endpoint.response.json()['name'])


def test_patch_a_object(
        create_patch_object_endpoint,
        create_get_object_id_endpoint,
        create_and_delete
):
    create_patch_object_endpoint.patch_object(payload={"name": "Jon"}, object_id=create_and_delete)
    create_patch_object_endpoint.check_status_code_200()
    create_get_object_id_endpoint.get_object_id(object_id=create_and_delete)
    create_get_object_id_endpoint.check_name(create_patch_object_endpoint.response.json()['name'])


def test_delete_a_object(create_delete_object_endpoint, create_object, create_get_object_id_endpoint):
    create_delete_object_endpoint.delete_object_id(object_id=create_object)
    create_delete_object_endpoint.check_status_code_200()
    create_get_object_id_endpoint.get_object_id(create_object)
    create_get_object_id_endpoint.check_status_code_404()
