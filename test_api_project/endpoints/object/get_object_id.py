import requests
import allure

from test_api_project.endpoints.object.base_object import Object


class GetObjectId(Object):

    @allure.step('Получение объекта по id')
    def get_object_id(self, object_id):
        self.response = requests.get(f'{self.url}/{object_id}')
        self.json = self.response.json()
        self.status_code = self.response.status_code
        return self.response

    @allure.step('Проверка имени')
    def check_name(self, name):
        assert self.json['name'] == name, 'The name does not match'
