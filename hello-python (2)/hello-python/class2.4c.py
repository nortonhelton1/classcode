# JSON the value can be 
# int, float, bool, dictionary, array 
# array of int, array of dictionary, array of bool etc 

import json 

# WRITE JSON 
with open("car.json", "w") as file: 
    car = {"make": "Honda", "model": "Accord", "noOfCylinders": 2}
    #json.dump(Object you want to write, file object)
    json.dump(car, file)



users = [] 

while True: 
    name = input("Enter name: ")
    age = int(input("Enter age: ")) 
    user = {"name": name, "age": age}

    users.append(user)

    with open("users.json", "w") as file:
         json.dump(users, file)
    
    choice = input("Q to quit or any key to continue: ")
    if choice == "q": 
        break 