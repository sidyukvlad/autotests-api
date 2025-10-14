import pytest

def test_user_login():
    pass

def test_first_try():
    print("hello")

def test_create_user():
    print("hello")

def test_assert_positive_case():
    assert (2 + 2) == 4

def test_assert_negative_case():
    x, y = 5, 2
    assert (x + y) == 5

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

class TestUserAuthentification:
    def test_create_user(self):
        pass
    def test_update_user(self):
        pass
