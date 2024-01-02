import json
import allure

from conftest import BASE_URL, PATH_LOGIN_COURIER, HEADERS
from req_post import req_post

courier_login = "dsyyfd"
courier_password = "gghghgh"
courier_id = 245873

courier_invalid_login = "dsyyfd1"
courier_invalid_password = "gghghgh1"

class TestCourierLogin:
    @allure.title('Проверка, что созданный курьер может авторизоваться')
    @allure.description('Тест проверяет, что при авторизации курьера запрос возвращает статус 200')
    def test_courier_authorization(self):
        payload = {"login": courier_login, "password": courier_password}

        response_raw = req_post(BASE_URL+PATH_LOGIN_COURIER, HEADERS, payload)

        assert response_raw.status_code == 200


    @allure.title('Проверка авторизации курьера без логина')
    @allure.description('Тест проверяет, что при авторизации курьера без логина запрос возвращает статус 400 и сообщение об ошибке')
    def test_courier_authorization_without_login(self):
        payload = {"password": courier_password}

        response_raw = req_post(BASE_URL + PATH_LOGIN_COURIER, HEADERS, payload)
        response_json = json.loads(response_raw.text)

        assert response_raw.status_code == 400
        assert response_json['message'] == "Недостаточно данных для входа"

    @allure.title('Проверка авторизации курьера с некорректным логином')
    @allure.description('Тест проверяет, что при авторизации курьера с некорректным логином запрос возвращает статус 404 и сообщение об ошибке')
    def test_courier_authorization_with_invalid_login(self):
        payload = {"login": courier_login, "password": courier_invalid_login}

        response_raw = req_post(BASE_URL + PATH_LOGIN_COURIER, HEADERS, payload)
        response_json = json.loads(response_raw.text)

        assert response_raw.status_code == 404
        assert response_json['message'] == "Учетная запись не найдена"

    @allure.title('Проверка авторизации курьера с некорректным паролем')
    @allure.description('Тест проверяет, что при авторизации курьера с некорректным паролем запрос возвращает статус 404 и сообщение об ошибке')
    def test_courier_authorization_with_invalid_password(self):
        payload = {"login": courier_login, "password": courier_invalid_password}

        response_raw = req_post(BASE_URL + PATH_LOGIN_COURIER, HEADERS, payload)
        response_json = json.loads(response_raw.text)

        assert response_raw.status_code == 404
        assert response_json['message'] == "Учетная запись не найдена"

    @allure.title('Проверка, что при успешной авторизации запрос возвращает id курьера')
    @allure.description('Тест проверяет, что при успешной авторизации запрос возвращает id курьера')
    def test_courier_id_under_success_authorization(self):
        payload = {"login": courier_login, "password": courier_password}

        response_raw = req_post(BASE_URL + PATH_LOGIN_COURIER, HEADERS, payload)
        response_json = json.loads(response_raw.text)

        assert response_json['id'] == courier_id
        
