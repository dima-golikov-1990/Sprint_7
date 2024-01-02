import json
import allure
import pytest

from conftest import BASE_URL, PATH_ORDER, HEADERS
from req_post import req_post

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
        payload = {"color": [""+ color +""]}

        response_raw = req_post(BASE_URL+PATH_ORDER, HEADERS, payload)

        assert response_raw.status_code == 201

    @allure.title('Проверка, что при создании заказа можно не указывать цвет')
    @allure.description('Тест проверяет что при создании заказа без указания цвет заказ выдаётся статус 201')
    def test_create_order_without_color(self):
        payload = {}

        response_raw = req_post(BASE_URL + PATH_ORDER, HEADERS, payload)

        assert response_raw.status_code == 201

    @allure.title('Проверка, что при создании заказа ответ содержит track')
    @allure.description('Тест проверяет что при создании заказа ответ содержит track')
    def test_answer_contains_track(self):
        payload = {}

        response_raw = req_post(BASE_URL + PATH_ORDER, HEADERS, payload)

        response_json = json.loads(response_raw.text)
        assert "track" in response_json
        
