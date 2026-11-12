import requests
import json
from pathlib import Path

try:
    response = requests.get("https://jsonplaceholder.typicode.com/users",
    timeout = 5)
    response.raise_for_status()
    # print(response.status_code)
    # print(response.text)
    data = response.json()
    print(data)
    Users = []
    for d in data:
        Users.append({
            "User_ID" : d["id"],
            "Name" : d["name"],
            "Username" : d["username"],
            "Email" : d["email"],
            "City" : d["address"],
            "Company" : d["company"]
        })

    with open("Users.json", "w") as file:
        json.dump(Users, file, indent= 8)

    json_path = Path("Users.json")

    if json_path.is_file():
        print("The file exists.")
    else:
        print("The file doesn't exist.")

    with open("Users.json", "r") as file:
        save_data= json.load(file)
        for s in save_data:
            print(s["User_ID"])
            print(s["Name"])
            print(s["Username"])
            print(s["Email"])
            print(s["City"])
            print(s["Company"])
        print(len(Users))
except requests.exceptions.ConnectionError:
    print("Could not connect to the server")
except requests.exceptions.Timeout:
    print("The Server took too long to respond.")
except requests.exceptions.HTTPError as error:
    print("Http error", error)
except requests.exceptions.RequestException as error:
    print("Request failed", error)
except KeyError as error:
    print("Missing fields", error)

