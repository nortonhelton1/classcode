
import json 

with open("movies.json") as file_object: 
    result = json.load(file_object)

movies = result["Search"] #movies will be an array of movies (dictionaries)

for movie in movies:
    print(movie["Title"])


 import json 

with open("users.json") as file_object: 
    users = json.load(file_object)

for user in users: 
    print(user["name"])
    print(user["age"])
    
    print(f"{user['name']} - {user['age']}") 

     import json 

# WRITE JSON 
#with open("car.json", "w") as file: 
#    car = {"make": "Honda", "model": "Accord", "noOfCylinders": 2}
    #json.dump(Object you want to write, file object)
#    json.dump(car, file)

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

# READ JSON 

with open("users.json") as file: 
    users = json.load(file)

for user in users: 
    print(user["name"])
    print(user["age"])   