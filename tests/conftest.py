import os
import django
import pytest
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from apps.accounts.models import CustomUser


django.setup()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")


@pytest.fixture
def api_client() -> APIClient:
    client = APIClient()
    user = CustomUser.objects.create(username="agent_smit", password="010110001")
    token = Token.objects.create(user=user)
    client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    return client


@pytest.fixture
def user() -> CustomUser:
    user = CustomUser.objects.create(username="neo", password="101010011")
    return user
