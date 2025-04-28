import requests
import allure


class Object:
    url = 'http://167.172.172.115:52353/object'
    response = None
    json = None
    status_code = None
    headers = {'Content-Type': 'application/json'}

    @allure.step('Проверка статуса ответа')
    def check_status_code(self):
        assert self.status_code < 300, 'Status cod is unexpected'
