import requests
import allure

from test_api_project.endpoints.object.base_object import Object


class DeleteObject(Object):

    @allure.step('Удаление объекта')
    def delete_object_id(self, object_id):
        self.response = requests.delete(f'{self.url}/{object_id}')
        self.status_code = self.response.status_code
        return self.response
