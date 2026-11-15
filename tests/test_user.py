from fastapi.testclient import TestClient

from user_server.main import app

client = TestClient(app)

# Существующие в БД пользователи
users = [
    {
        'id': 1,
        'name': 'Ivan Ivanov',
        'email': 'i.i.ivanov@mail.com',
    },
    {
        'id': 2,
        'name': 'Petr Petrov',
        'email': 'p.p.petrov@mail.com',
    }
]

def test_get_existed_user():
    """Получение существующего пользователя"""
    response = client.get("/api/v1/user", params={'email': users[0]['email']})
    assert response.status_code == 200
    assert response.json() == users[0]

def test_get_unexisted_user():
    """Получение несуществующего пользователя"""
    response = client.get("/api/v1/user", params={'email': users[2]['email']})
    assert response.status_code == 404

def test_create_user_with_valid_email():
    """Создание пользователя с уникальной почтой"""
    pass

def test_create_user_with_exist_email():
    """Создание пользователя с почтой, которую использует другой пользователь"""
    pass

def test_update_user_name():
    """Изменение имени пользователя"""
    pass

def test_delete_user():
    """Удаление пользователя"""
    pass