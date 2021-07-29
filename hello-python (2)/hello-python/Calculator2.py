number = int(input("Please input your number: "))

def even_odd(x):
    if x % 2 == 0:
        return "Your number is even."
    else:
        return "Your number is odd."

which = even_odd(number)
print(which)