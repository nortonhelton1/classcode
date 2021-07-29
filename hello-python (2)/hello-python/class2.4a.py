{   
    "totalCustomers": 300, 
    "lastCustomerAdded": "02/11/2021",
    "customers": [
        {
            "firstName": "John", 
            "lastName": "Doe"
        }, 
        {
            "firstName": "Mary", 
            "lastName": "Doe"
        }
    ]
}

 {"name": "John", "age": 34, "addresses": [{"street": "1200 Richmond"}]},
    {"name": "Mary", "age": 56}
]

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