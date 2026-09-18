import pytest


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (10, 20, 30),
    (0, 0, 0),
    (100, 50, 150),
])
def test_add(a, b, expected):
    assert a + b == expected