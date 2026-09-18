import requests


def test_get_github_user():
    response = requests.get("https://api.github.com/users/torvalds")

    ("Статус:", response.status_code)

    data = response.json()
    ("Логин:", data["login"])
    ("ID:", data["id"])
    ("Тип:", data["type"])

    assert response.status_code == 200
    assert data["login"] == "torvalds"
    assert data["type"] == "User"