
import json 

users = [] 

while True: 
    name = input("Enter name: ")
    age = int(input("Enter age: "))

    # write name and age to a JSON doc 
    with open("users.json", "w") as file_object: 
        user = {"name": name, "age": age}
        users.append(user)
        json.dump(users, file_object)

    choice = input("Press q to quit or any key to continue: ")
    if choice == "q": 
        break 

