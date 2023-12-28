import requests
import json
import allure
import pytest

base_url = "https://qa-scooter.praktikum-services.ru/"
path = "api/v1/orders"

class TestCreateOrder:
    @pytest.mark.parametrize(
        'color',
        [
            "BLACK", "GREY"
        ]
    )
    @allure.title('Проверка что при создании заказа можно указать цвет BLACK и GREY')
    @allure.description('Тест проверяет что при создании заказа с цветами BLACK и GREY в ответе код 201')
    def test_create_order_with_color(self, color):
        headers = {"accept": "application/json", "Content-Type": "application/json"}
        payload = {"color": [""+ color +""]}
        response_raw = requests.post(url=base_url+path,
                                     headers=headers,
                                     data=json.dumps(payload))
        assert response_raw.status_code == 201

    @allure.title('Проверка, что при создании заказа можно не указывать цвет')
    @allure.description('Тест проверяет что при создании заказа без указания цвет заказ выдаётся статус 201')
    def test_create_order_without_color(self):
        headers = {"accept": "application/json", "Content-Type": "application/json"}
        payload = {}
        response_raw = requests.post(url=base_url + path,
                                     headers=headers,
                                     data=json.dumps(payload))
        assert response_raw.status_code == 201

    @allure.title('Проверка, что при создании заказа ответ содержит track')
    @allure.description('Тест проверяет что при создании заказа ответ содержит track')
    def test_answer_contains_track(self):
        headers = {"accept": "application/json", "Content-Type": "application/json"}
        payload = {}
        response_raw = requests.post(url=base_url + path,
                                     headers=headers,
                                     data=json.dumps(payload))
        response_json = json.loads(response_raw.text)
        assert "track" in response_json