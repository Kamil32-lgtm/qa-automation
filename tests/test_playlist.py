def total_duration(tracks):
    total = 0
    for track in tracks:
        total = total + track["duration"]
    return total


def test_total_duration():
    tracks = [
        {"title": "Song of the Ancients", "duration": 215, "mood": "calm"},
        {"title": "Proof of a Hero", "duration": 320, "mood": "epic"},
        {"title": "Unshaken", "duration": 245, "mood": "calm"},
        {"title": "Devil Trigger", "duration": 290, "mood": "epic"},
    ]
    assert total_duration(tracks) == 1070


def filter_by_mood(tracks, mood):
    result = []
    for track in tracks:
        if track["mood"] == mood:
            result.append(track)
    return result


def test_filter_by_mood():
    tracks = [
        {"title": "Song of the Ancients", "duration": 215, "mood": "calm"},
        {"title": "Proof of a Hero", "duration": 320, "mood": "epic"},
        {"title": "Unshaken", "duration": 245, "mood": "calm"},
        {"title": "Devil Trigger", "duration": 290, "mood": "epic"},
    ]
    epic_tracks = filter_by_mood(tracks, "epic")
    assert len(epic_tracks) == 2
    assert epic_tracks[0]["title"] == "Proof of a Hero"
    assert epic_tracks[1]["title"] == "Devil Trigger"


def longest_track(tracks):
    longest = tracks[0]
    for track in tracks:
        if track["duration"] > longest["duration"]:
            longest = track
    return longest


def test_longest_track():
    tracks = [
        {"title": "Song of the Ancients", "duration": 215, "mood": "calm"},
        {"title": "Proof of a Hero", "duration": 320, "mood": "epic"},
        {"title": "Unshaken", "duration": 245, "mood": "calm"},
        {"title": "Devil Trigger", "duration": 290, "mood": "epic"},
    ]
    longest = longest_track(tracks)
    assert longest["title"] == "Proof of a Hero"
    assert longest["duration"] == 320