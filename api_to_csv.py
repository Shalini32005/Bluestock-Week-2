
import urllib.request
import json
import csv

url = "https://jsonplaceholder.typicode.com/users"

response = urllib.request.urlopen(url)
data = json.loads(response.read().decode())

with open("users.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["ID", "Name", "Username", "Email", "City"])

    for user in data:
        writer.writerow([
            user["id"],
            user["name"],
            user["username"],
            user["email"],
            user["address"]["city"]
        ])

print("API data successfully converted into CSV!")
