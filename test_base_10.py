track = {
        "title":"Proof of a Hero", 
        "duration": 320, 
        "mood": "epic",
}


print(track["title"])
print(track["duration"])
print(track["mood"])


print("title" in track)
print("artist" in track)


for key, value in track.items():
    print(key, value)