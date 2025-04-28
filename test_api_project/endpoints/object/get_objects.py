import requests
import allure
from test_api_project.endpoints.object.base_object import Object


class GetObjects(Object):

    @allure.step('Получение всех объектов')
    def get_all_objects(self):
        self.response = requests.get(self.url)
        self.json = self.response.json()
        self.status_code = self.response.status_code
        return self.response

    @allure.step('Проверка объектов в ответе')
    def check_objects_in_response(self):
        assert self.json != {}, 'Objects not found'
