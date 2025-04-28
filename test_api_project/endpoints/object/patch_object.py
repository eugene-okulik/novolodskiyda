import requests
import allure
from test_api_project.endpoints.object.base_object import Object


class PatchObject(Object):

    @allure.step('Частичное изменение объекта')
    def patch_object(self, object_id, payload, headers=None):
        headers_patch = headers if headers else self.headers
        self.response = requests.patch(url=f'{self.url}/{object_id}', json=payload, headers=headers_patch)
        self.json = self.response.json()
        self.status_code = self.response.status_code
        return self.response

    @allure.step('Проверка изменения имени')
    def check_name(self, name):
        assert self.json['name'] == f'{name}', 'Method did not change name'
