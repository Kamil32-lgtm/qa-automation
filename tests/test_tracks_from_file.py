import json
from pathlib import Path


def load_tracks():
    file_path = Path(__file__).parent / "tracks.json"
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def total_duration(tracks):
    total = 0
    for track in tracks:
        total = total + track["duration"]
    return total


def test_total_from_file():
    tracks = load_tracks()
    assert len(tracks) == 5
    assert total_duration(tracks) == 1470


def test_longest_from_file():
    tracks = load_tracks()
    longest = tracks[0]
    for track in tracks:
        if track["duration"] > longest["duration"]:
            longest = track
    assert longest["title"] == "Weight of the World"
    assert longest["duration"] == 400