import pytest


@pytest.mark.parametrize("username,password",
                         [
                             ("user", "pass"),
                             ("abc", "abc@1234"),
                             ("dcs", "dcs@1234"),
                             ("pdr", "pdr@12345")
                         ]
                         )
def test_login(username, password):
    print(username + " " + password)
