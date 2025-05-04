import requests
import allure
from test_api_project.endpoints.object.base_object import Object


class PostObject(Object):

    @allure.step('Создание нового объекта')
    def post_object(self, payload, headers=None):
        headers_post = headers if headers else self.headers
        self.response = requests.post(url=self.url, json=payload, headers=headers_post)
        self.status_code = self.response.status_code
        return self.response

    @allure.step('Проверка имени в ответе')
    def check_name_in_response(self, name):
        assert self.response.json()['name'] == name, 'The name does not match'

    @allure.step('Проверка всех полей в ответе')
    def check_all_fields_in_response(self, test_data):
        response_data = self.response.json()
        assert response_data['name'] == test_data['name'], 'The name does not match'
        assert response_data['data']['color'] == test_data['data']['color'], 'The color does not match'
        assert response_data['data']['country'] == test_data['data']['country'], 'The country does not match'
