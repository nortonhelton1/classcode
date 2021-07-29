with open("users.json", "w") as file:
    users =[]

while True:

    if name == "q":
        break
    name = input("Enter your name:")
    age = int(input("Enter your age:"))
    person_dict = ("name": name, "age" age)
    users.append(person_dict)

json.dump(users, file)

