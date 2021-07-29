with open("emails.txt") as file_object: 
    emails = file_object.read()


# convert string comma separated into an array
duplicate_emails = emails.split(',')

#print(duplicate_emails)

# final array containing NO DUPLICATES 
duplicate_free_emails = [] 

for email in duplicate_emails: 
    email = email.strip() 
    if email not in duplicate_free_emails: 
        duplicate_free_emails.append(email)

# Using For Index Loop
#for index in range(0, len(duplicate_emails)): 
#    email = duplicate_emails[index]
#    if email not in duplicate_free_emails: 
#        duplicate_free_emails.append(email)


# write to the duplicate free emails text file 
with open("duplicate-free-emails.txt", "w") as file_object:
    for email in duplicate_free_emails: 
        file_object.write(email)
        file_object.write("\n") 
    
    


