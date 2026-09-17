def longest_game(games):
    longest = games[0]
    for game in games:
        if game["hours"] > longest["hours"]:
            longest = game
    return longest


games = [
    {"name": "RDR2", "hours": 150},
    {"name": "Monster Hunter World", "hours": 350},
    {"name": "Dying Light", "hours": 80},
]

result = longest_game(games)
print(result["name"])
print(result["hours"])