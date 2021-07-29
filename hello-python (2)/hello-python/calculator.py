first_number = int(input("Enter the first number: "))
operand = input("Enter the mathmatecial operation: ")
second_number = int(input("Enter the second number: "))


def calculator(x, operation, y):
    if operation == "+" :
        return x + y
    elif operation == "-" :
        return x - y
    elif operation == "*" :
        return x * y
    else:
        return x/y

answer = calculator(first_number, operand, second_number)
print(answer)
