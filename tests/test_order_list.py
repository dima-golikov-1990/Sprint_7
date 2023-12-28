import requests
import json
import allure

base_url = "https://qa-scooter.praktikum-services.ru/"
path = "api/v1/orders"

fields_in_order = {"id", "courierId", "firstName", "lastName", "address", "metroStation", "phone", "rentTime", "deliveryDate", "track", "color", "comment", "createdAt", "updatedAt", "status"}

class TestOrderList:
    @allure.title('Проверка, что при запросе списка заказов возвращается список')
    @allure.description('Тест проверяет, что при запросе списка заказов возвращается список')
    def test_answer_body_contains_order_list(self):
        headers = {"accept": "application/json", "Content-Type": "application/json"}
        payload = {}
        response_raw = requests.get(url=base_url+path,
                                     headers=headers,
                                     data=json.dumps(payload))
        response_json = json.loads(response_raw.text)
        assert isinstance(response_json['orders'], list) == True
        assert response_raw.status_code == 200