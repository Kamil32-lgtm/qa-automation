import requests


def test_user_not_found():
    response = requests.get("https://api.github.com/users/this-user-does-not-exist-99999")
    assert response.status_code == 404
