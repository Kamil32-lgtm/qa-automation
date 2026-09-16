import json
import pytest


def load_tracks():
    with open("tracks.json", "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.mark.parametrize("track", load_tracks())
def test_track_is_valid(track):
    assert "title" in track
    assert "duration" in track
    assert "mood" in track
    assert track["duration"] > 0
    assert track["mood"] in ["calm", "epic", "sad", "happy"]


@pytest.mark.parametrize("track", load_tracks())
def test_track_title_is_string(track):
    assert isinstance(track["title"], str)
    assert len(track["title"]) > 0
