import json
import allure
from conftest import BASE_URL, PATH_COURIER, HEADERS

from register_courier import register_new_courier_and_return_login_password
from req_post import req_post

courier_data = register_new_courier_and_return_login_password()

class TestCreateCourier:
    @allure.title('Проверка, что курьера можно создать')
    @allure.description('Тест проверяет что при создании курьера в ответе код 201')
    def test_create_courier(self):
        payload = {"login": courier_data[0] + '1', "password": courier_data[1] + '2', "firstName": courier_data[2] + '3'}

        response_raw = req_post(BASE_URL+PATH_COURIER, HEADERS, payload)

        assert response_raw.status_code == 201

    @allure.title('Проверка, что нельзя создать двух одинаковых курьеров')
    @allure.description('Тест проверяет что при создании курьера с ранее использованными данными выдаётся код 409 и сообщение об ошибке')
    def test_create_two_couriers_with_same_data(self):
        payload = {"login": courier_data[0], "password": courier_data[1], "firstName": courier_data[2]}

        req_post(BASE_URL + PATH_COURIER, HEADERS, payload)
        response_raw = req_post(BASE_URL + PATH_COURIER, HEADERS, payload)
        response_json = json.loads(response_raw.text)

        assert response_raw.status_code == 409
        assert response_json['message'] == "Этот логин уже используется. Попробуйте другой."

    @allure.title('Проверка, что нельзя создать курьера без логина')
    @allure.description('Тест проверяет что при создании курьера без логина выдаётся код 400 и сообщение об ошибке')
    def test_create_courier_without_login(self):
        payload = {"password": courier_data[1], "firstName": courier_data[2]}

        response_raw = req_post(BASE_URL + PATH_COURIER, HEADERS, payload)
        response_json = json.loads(response_raw.text)

        assert response_raw.status_code == 400
        assert response_json['message'] == "Недостаточно данных для создания учетной записи"

    @allure.title('Проверка, что нельзя создать курьера без пароля')
    @allure.description('Тест проверяет что при создании курьера без пароля выдаётся код 400 и сообщение об ошибке')
    def test_create_courier_without_password(self):
        payload = {"login": courier_data[0], "firstName": courier_data[2]}

        response_raw = req_post(BASE_URL + PATH_COURIER, HEADERS, payload)
        response_json = json.loads(response_raw.text)

        assert response_raw.status_code == 400
        assert response_json['message'] == "Недостаточно данных для создания учетной записи"

    @allure.title('Проверка, что успешный запрос возвращает {"ok":true}')
    @allure.description('Тест проверяет что при создании курьера в ответе {"ok":true}')
    def test_create_courier_flag_equal_true(self):
        payload = {"login": courier_data[0] + '4', "password": courier_data[1] + '5', "firstName": courier_data[2] + '6'}

        response_raw = req_post(BASE_URL + PATH_COURIER, HEADERS, payload)
        response_json = json.loads(response_raw.text)

        assert response_json['ok']

    @allure.title('Проверка, что нельзя создать двух курьеров с одинаковым логином')
    @allure.description('Тест проверяет что при создании двух курьеров с одинаковым логином выдаётся код 409 и сообщение об ошибке')
    def test_create_two_couriers_with_same_data(self):
        payload = {"login": courier_data[0], "password": courier_data[1], "firstName": courier_data[2]}

        response_raw = req_post(BASE_URL + PATH_COURIER, HEADERS, payload)
        response_json = json.loads(response_raw.text)

        assert response_raw.status_code == 409
        assert response_json['message'] == "Этот логин уже используется. Попробуйте другой."
