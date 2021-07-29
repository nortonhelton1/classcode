
# EXCEPTIONS 
# try and except go together 

#result = int(input("Enter number: "))

def add(a,b): 
    result = 100/0 

try: 
    add(2,3)
    result = 1/2
    number = int(input("Enter any number: "))  # e 
except ZeroDivisionError: 
    print("Please don't divide by zero!")
except ValueError: 
    print("Invalid input. Please enter numbers only!")
except: 
    print("Opps!!")
else: # optional block. Fired when no exceptions are thrown 
    print("ELSE BLOCK")
# finally is an optional block which executes whether exception takes place or NOT 
finally: 
    # finally block is where to close out the resources 
    print("FINALLY!")

print("CONTINUE....")




