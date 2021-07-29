
import json 

with open("users.json") as file_object: 
    users = json.load(file_object)

for user in users: 
    print(user["name"])
    print(user["age"])
    
    print(f"{user['name']} - {user['age']}")