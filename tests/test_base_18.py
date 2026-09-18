import requests

response = requests.get("https://api.github.com/users/torvalds/repos")
data = response.json()

print("Статус:", response.status_code)
print("Тип:", type(data))
print("Всего репозиториев:", len(data))
print()

for repo in data:
    print(repo["name"])