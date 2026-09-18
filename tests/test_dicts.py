def test_dict_basics():
    user = {"name": "Kamil", "age": 25}
    assert user["name"] == "Kamil"
    assert user["age"] == 25
    assert "name" in user
    assert "phone" not in user


def test_dict_modify():
    user = {"name": "Kamil"}
    user["age"] = 25
    user["city"] = "Moscow"
    assert user["age"] == 25
    assert user["city"] == "Moscow"
    assert len(user) == 3


def test_dict_get():
    user = {"name": "Kamil"}
    assert user.get("name") == "Kamil"
    assert user.get("phone", "не указан") == "не указан"
    assert user.get("phone") is None


def test_nested_dict():
    response = {
        "status": "ok",
        "user": {
            "id": 152,
            "name": "Kamil",
            "roles": ["admin", "user"],
        },
    }
    assert response["status"] == "ok"
    assert response["user"]["name"] == "Kamil"
    assert response["user"]["roles"][0] == "admin"
    assert "admin" in response["user"]["roles"]
    assert response["user"]["id"] == 152
    assert response["user"]["roles"][1] == "user"

def test_dict_loop():
    user = {"name": "Kamil", "age": 25}
    keys = []
    for key in user:
        keys.append(key)
    assert "name" in keys
    assert "age" in keys
    assert len(keys) == 2
    