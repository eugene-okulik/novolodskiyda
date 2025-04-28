import requests
import allure
from test_api_project.endpoints.object.base_object import Object


class PostObject(Object):

    @allure.step('Создание нового объекта')
    def post_object(self, payload, headers=None):
        headers_post = headers if headers else self.headers
        self.response = requests.post(url=self.url, json=payload, headers=headers_post)
        self.json = self.response.json()
        self.status_code = self.response.status_code
        return self.response

    @allure.step('Проверка имени в ответе')
    def check_name_in_response(self, name):
        assert self.json['name'] == name, 'The name does not match'
