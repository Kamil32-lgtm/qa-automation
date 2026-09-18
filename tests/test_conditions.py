def test_adult():
    age = 20
    if age >= 18:
        result = "adult"
    else:
        result = "child"
    assert result == "adult"


def test_grades():
    score = 75
    if score >= 90:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
    assert grade == "B"


def test_membership():
    statuses = ["new", "paid", "shipped"]
    assert "paid" in statuses
    assert "cancelled" not in statuses


def test_in_string():
    response = "User created successfully"
    assert "successfully" in response
    assert "error" not in response.lower()
    