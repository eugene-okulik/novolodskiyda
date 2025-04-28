import requests
import allure
from test_api_project.endpoints.object.base_object import Object


class PutObject(Object):

    @allure.step('Полное изменение объекта')
    def put_object(self, object_id, payload, headers=None):
        headers_put = headers if headers else self.headers
        self.response = requests.put(url=f'{self.url}/{object_id}', json=payload, headers=headers_put)
        self.json = self.response.json()
        self.status_code = self.response.status_code
        return self.response

    @allure.step('Проверка id в ответе')
    def check_id_in_response(self, object_id):
        assert self.json['id'] == f'{object_id}', 'Object id is not true'
