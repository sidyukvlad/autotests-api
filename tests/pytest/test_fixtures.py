import pytest

@pytest.fixture
def users_client():
    print()

# Определение фикстуры
@pytest.fixture
def sample_fixture():
    return {"key": "value"}

# Использование фикстуры в тесте
def test_using_fixture(sample_fixture):
    assert sample_fixture["key"] == "value"


@pytest.fixture
def user_data():
    return {"username": "test_user", "email": "test@example.com"}

def test_user_email(user_data):
    assert user_data["email"] == "test@example.com"

def test_user_username(user_data):
    assert user_data["username"] == "test_user"