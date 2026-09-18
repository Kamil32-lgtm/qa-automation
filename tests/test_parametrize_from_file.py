import json
import pytest
from pathlib import Path


def load_tracks():
    file_path = Path(__file__).parent / "tracks.json"
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.mark.parametrize("track", load_tracks(), ids=lambda t: t["title"])
def test_track_is_valid(track):
    assert "title" in track
    assert "duration" in track
    assert "mood" in track
    assert track["duration"] > 0
    assert track["mood"] in ["calm", "epic", "sad", "happy"]


@pytest.mark.parametrize("track", load_tracks(), ids=lambda t: t["title"])
def test_track_title_is_string(track):
    assert isinstance(track["title"], str)
    assert len(track["title"]) > 0
