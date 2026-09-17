import pytest
import requests


@pytest.fixture
def github_user():
    response = requests.get("https://api.github.com/users/torvalds")
    return response.json()


def test_login(github_user):
    assert github_user["login"] == "torvalds"


def test_id(github_user):
    assert github_user["id"] == 1024025


def test_type(github_user):
    assert github_user["type"] == "User"


def test_has_repos(github_user):
    assert "public_repos" in github_user