import pytest
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_extra.testing import TestClient

from tasktastic.user.tests.factories import UserFactory


@pytest.fixture
def authenticated_user():
    """
    Returns an authenticated test user.
    Usage: authenticated_user() -> user
    """

    def _factory():
        user = UserFactory()
        client = TestClient(NinjaJWTDefaultController)
        response = client.post('/pair', json={"username": user.username, "password": "defaultpassword"})
        assert response.status_code == 200, response.json()
        token = response.json().get("access")
        return user, token

    return _factory