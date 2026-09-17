games = ["RDR2", "Monster Hunter World", "Dying Light", "Dark Souls"]


print(games[-1])   


print(games[1])   


games.append("Elden Ring") 


for game in games:
    print(game)


def is_valid_status(status):
    return status in ["new", "paid", "shipped", "cancelled"]

print(is_valid_status("paid"))      
print(is_valid_status("hacked"))    