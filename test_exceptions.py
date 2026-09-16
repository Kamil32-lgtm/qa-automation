import json
import logging
import pytest


log = logging.getLogger(__name__)


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0


def test_invalid_int_conversion():
    with pytest.raises(ValueError):
        int("abc")


def test_invalid_json():
    with pytest.raises(json.JSONDecodeError):
        json.loads("{невалидный json")


def test_missing_key():
    user = {"name": "Kamil"}
    with pytest.raises(KeyError):
        user["email"]


def test_index_out_of_range():
    tracks = ["Song of the Ancients", "Proof of a Hero"]
    with pytest.raises(IndexError):
        tracks[10]


def test_error_message_contains():
    with pytest.raises(ValueError, match="invalid"):
        raise ValueError("invalid input from user")


def test_error_object():
    with pytest.raises(ValueError) as exc_info:
        raise ValueError("Что-то пошло не так")

    assert "не так" in str(exc_info.value)
    log.info(f"Поймали ошибку: {exc_info.value}")


def test_no_exception_expected():
    # Когда ошибки НЕ должно быть — обычный assert
    result = int("42")
    assert result == 42