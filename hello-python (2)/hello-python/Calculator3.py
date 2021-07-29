number = int(input("Enter your number :"))

def fizz_buzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return "Fizz Buzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return "This number is neither divisible by 3 or 5."

answer = fizz_buzz(number)
print(answer)