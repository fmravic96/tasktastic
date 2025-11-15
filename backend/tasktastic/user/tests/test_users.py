import pytest
from ninja_extra.testing import TestClient

from tasktastic.user.controllers import UserModelController
from tasktastic.user.tests.factories import UserFactory


@pytest.mark.django_db
class TestUserModelController:
    def test_create_user(self):
        client = TestClient(UserModelController)
        payload = {
            "username": "testuser",
            "password": "securepassword123",
            "email": "test@example.com",
            "first_name": "Test",
            "last_name": "User"
        }
        response = client.post('', json=payload)
        assert response.status_code == 201, response.json()

    def test_get_user(self):
        client = TestClient(UserModelController)
        user = UserFactory()
        response = client.get(f'/{user.id}')
        assert response.status_code == 200, response.json()