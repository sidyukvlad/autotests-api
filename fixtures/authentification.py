from clients.authentification.authentification_client import get_authentification_client, AuthentificationClient
import pytest

@pytest.fixture
def authentification_client() -> AuthentificationClient:
    return get_authentification_client()


