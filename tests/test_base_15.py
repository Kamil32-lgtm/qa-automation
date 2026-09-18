import pytest
import requests 


@pytest.mark.parametrize("username, expected_status",[
("torvalds", 200),
("this-user-does-not-exist-99999", 404),
])


def test_github_user(username, expected_status):
    response = requests.get(f"https://api.github.com/users/{username}")
    assert response.status_code == expected_status