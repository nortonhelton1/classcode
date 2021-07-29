# WRITING TO A FILE 

# open(name of the file, mode) By default mode is "r"

# w = Writing a file 
# r = Reading a file 
# a = Appending mode 

# OPTION 1

# opening the file for writing, create a file if does not exist or overrite if exist  
#file = open("todo.txt","w") 

# write text to a file 
#file.write("Clean the car")

# ALWAYS close the file 
#file.close() 

# OPTION 2 
# with operator is going to call close() automatically at the end of with body

#with open("todo.txt", "w") as file: 
#    file.write("Mow the lawn \n")
#    file.write("Clean the car \n")
#    file.write("Do dishes")

#task_name = input("Enter todo list task: ")
#with open("todo.txt", "a") as file: 
#    file.write(task_name)
#    file.write("\n")

# READING A FILE 

# read all the contents of a file and return as string 
 # default mode is "r"
#with open("todo.txt") as file_object:
    # read function allows to read everything from a file 
#    content = file_object.read()

#print(content)

# readlines is going to return an array of lines in the file 
with open("todo.txt") as file_object: 
    lines = file_object.readlines()

print(lines)

