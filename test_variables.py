def test_int_operations():
    a = 10
    b = 3
    assert a + b == 13
    assert a - b == 7
    assert a * b == 30
    assert a // b == 3
    assert a % b == 1


def test_string_operations():
    first = "Hello"
    second = "World"
    assert first + " " + second == "Hello World"
    assert first.upper() == "HELLO"
    assert first.lower() == "hello"
    assert len(first) == 5


def test_types():
    name = "Kamil"
    age = 25
    price = 99.5
    is_student = True

    assert isinstance(name, str)
    assert isinstance(age, int)
    assert isinstance(price, float)
    assert isinstance(is_student, bool)



def test_my_first_own_test():
    x = 7
    y = 2
    assert x + y == 9
    assert x - y == 5
    assert x * y == 14
    assert x % y == 1