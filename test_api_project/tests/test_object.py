def test_get_objects(create_get_objects_endpoint):
    create_get_objects_endpoint.get_all_objects()
    create_get_objects_endpoint.check_objects_in_response()
    create_get_objects_endpoint.check_status_code()


def test_get_object_id(create_get_object_id_endpoint, create_post_object_endpoint, generated_post_data):
    create_post_object_endpoint.post_object(generated_post_data)
    create_get_object_id_endpoint.get_object_id(create_post_object_endpoint.json['id'])
    create_get_object_id_endpoint.check_status_code()
    create_get_object_id_endpoint.check_name(name=create_post_object_endpoint.json['name'])


def test_post_object(
        create_post_object_endpoint,
        create_get_object_id_endpoint,
        create_delete_object_endpoint,
        generated_post_data
):
    create_post_object_endpoint.post_object(generated_post_data)
    create_post_object_endpoint.check_status_code()
    create_post_object_endpoint.check_name_in_response(generated_post_data['name'])
    create_get_object_id_endpoint.get_object_id(create_post_object_endpoint.json['id'])
    create_get_object_id_endpoint.check_name(create_post_object_endpoint.json['name'])
    create_delete_object_endpoint.delete_object_id(create_post_object_endpoint.json['id'])


def test_put_a_object(
        create_put_object_endpoint,
        create_get_object_id_endpoint,
        create_delete_object_endpoint,
        create_post_object_endpoint,
        generated_post_data,
        generated_put_data
):
    create_post_object_endpoint.post_object(generated_post_data)
    create_put_object_endpoint.put_object(payload=generated_put_data, object_id=create_post_object_endpoint.json['id'])
    create_put_object_endpoint.check_status_code()
    create_get_object_id_endpoint.get_object_id(create_post_object_endpoint.json['id'])
    create_get_object_id_endpoint.check_name(create_put_object_endpoint.json['name'])
    create_delete_object_endpoint.delete_object_id(object_id=create_post_object_endpoint.json['id'])


def test_patch_a_object(
        create_patch_object_endpoint,
        create_get_object_id_endpoint,
        create_post_object_endpoint,
        create_delete_object_endpoint,
        generated_post_data
):
    create_post_object_endpoint.post_object(generated_post_data)
    create_patch_object_endpoint.patch_object(payload={"name": "Jon"}, object_id=create_post_object_endpoint.json['id'])
    create_patch_object_endpoint.check_status_code()
    create_get_object_id_endpoint.get_object_id(object_id=create_post_object_endpoint.json['id'])
    create_get_object_id_endpoint.check_name(create_patch_object_endpoint.json['name'])
    create_delete_object_endpoint.delete_object_id(object_id=create_post_object_endpoint.json['id'])


def test_delete_a_object(create_delete_object_endpoint, create_post_object_endpoint, generated_post_data):
    create_post_object_endpoint.post_object(generated_post_data)
    create_delete_object_endpoint.delete_object_id(object_id=create_post_object_endpoint.json['id'])
    create_delete_object_endpoint.check_status_code()
