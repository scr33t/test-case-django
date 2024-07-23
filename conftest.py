import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass


@pytest.fixture()
def api_client():
    return APIClient()


@pytest.fixture()
def logged_user(api_client):
    user = User.objects.create()

    api_client.force_authenticate(user)

    return user
