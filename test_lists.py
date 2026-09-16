def test_list_basics():
    tracks = ["Song of the Ancients", "Proof of a Hero", "Unshaken"]
    assert tracks[0] == "Song of the Ancients"
    assert tracks[-1] == "Unshaken"
    assert len(tracks) == 3


def test_append_and_in():
    tracks = ["Song of the Ancients", "Proof of a Hero"]
    tracks.append("Devil Trigger")
    assert len(tracks) == 3
    assert "Devil Trigger" in tracks
    assert "Nonexistent" not in tracks


def test_loop():
    scores = [10, 20, 30]
    total = 0
    for score in scores:
        total = total + score
    assert total == 60


def test_loop_check_each():
    statuses = ["paid", "paid", "shipped"]
    for status in statuses:
        assert status in ["new", "paid", "shipped", "cancelled"]


def test_loop_with_index():
    tracks = ["a", "b", "c"]
    result = []
    for i, track in enumerate(tracks):
        result.append(f"{i}:{track}")
    assert result == ["0:a", "1:b", "2:c"]