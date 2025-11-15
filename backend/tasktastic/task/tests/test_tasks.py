import datetime

import pytest
from ninja_extra.testing import TestClient

from tasktastic.task.controllers import TaskModelController


@pytest.mark.django_db
class TestTaskModelController:
    def test_create_task(self, authenticated_user):
        client = TestClient(TaskModelController)
        user, token = authenticated_user()
        client.headers['Authorization'] = f'Bearer {token}'
        payload = {
            "title": "Test Task",
            "description": "This is a test task.",
            "category": "Testing",
            "due": datetime.datetime.utcnow(),
            "user_id": str(user.id)
        }
        response = client.post('', json=payload, headers=client.headers)
        assert response.status_code == 201, response.json()

    def test_get_task(self, task_client, task):
        response = task_client.get(f'/{task.id}')
        assert response.status_code == 200, response.json()