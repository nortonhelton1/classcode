
# JSON the value can be 
# int, float, bool, dictionary, array 
# array of int, array of dictionary, array of bool 

import json 

# Write JSON 
#with open("car.json", "w") as file_object: 
    #json.dump(Object you want to write int, float, string, array, dict, file_object)
#    car = {"make": "Honda", "model": "Accord"}
#    json.dump(car, file_object) # {make: "Honda", model: "Accord"}

with open("car.json") as file_object: 
    car = json.load(file_object)

print(car)



with open("users.json") as file_object: 
   users = json.load(file_object)

print(users)

#Name: John 
#Age: 34 

#Name: Mary 
#Age: 45 


