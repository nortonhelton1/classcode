first_number = float(input("Please enter your first number: "))
print("Now pick an opertaor:")
operator = input()
second_number = float(input("Now your second number: "))

if operator == "+":
    addition = first_number + second_number
    print (addition)
elif operator == "-":
    subtraction = first_number - second_number
    print (subtraction)
elif operator == "*":
    multiplication = first_number * second_number
    print(multiplication)
elif operator == "/":
    division = first_number // second_number
    print(division)
else:
    print("error")