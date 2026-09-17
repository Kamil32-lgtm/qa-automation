games = [
    {"name": "RDR2", "hours": 150, "rating": 9.8},
    {"name": "Monster Hunter World", "hours": 350, "rating": 9.5},
    {"name": "Dying Light", "hours": 80, "rating": 8.5},
]


print(games[0]["name"])

print(games[1]["hours"])

print(games[-1]["rating"])

for game in games:
    print(f"{game['name']} - {game['hours']} ч.")