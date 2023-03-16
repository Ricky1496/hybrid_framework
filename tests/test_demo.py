import pytest


class TestDemo:



    data = [
        ("paul", "paul123"),
        ("john", "john123")
    ]

    @pytest.mark.parametrize("username, password", data)
    def test_valid_login(self, username, password):
        print("valid login", username, password)