def add(a, b):
    return a + b


def is_valid_status(status):
    return status in ["new", "paid", "shipped", "cancelled"]


def count_valid(statuses):
    total = 0
    for status in statuses:
        if is_valid_status(status):
            total = total + 1
    return total


def test_add():
    assert add(2, 3) == 5
    assert add(10, 20) == 30
    assert add(-1, 1) == 0


def test_is_valid_status():
    assert is_valid_status("paid") is True
    assert is_valid_status("cancelled") is True
    assert is_valid_status("hacked") is False


def test_count_valid():
    statuses = ["paid", "hacked", "shipped", "unknown"]
    assert count_valid(statuses) == 2



def multiply (a, b):
    return a * b


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6