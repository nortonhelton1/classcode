int(input("Enter a number"))

try:
    result = 1/6
    number = int(input("Enter Number:"))
    #database.open()
    #do something with database
    #database.Close()
    #zero division block


except ZeroDivisionError:
    print("Divided by ZERO!")

except ValueError:
    print("only numbers")

except:
    print("Opps something bad happened")


