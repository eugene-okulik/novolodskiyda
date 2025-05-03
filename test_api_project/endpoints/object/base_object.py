import requests
import allure


class Object:
    url = 'http://167.172.172.115:52353/object'
    response = None
    status_code = None
    headers = {'Content-Type': 'application/json'}
    object_id = None

    @allure.step('Проверка успешного статуса ответа (200)')
    def check_status_code_200(self):
        assert self.status_code < 300, 'Status code is unexpected'

    @allure.step('Проверка статуса ответа 404')
    def check_status_code_404(self):
        assert self.status_code == 404, 'Status code is not 404'
