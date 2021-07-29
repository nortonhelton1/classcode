email_list = []

with open("emails.txt", "a") as file_object:
    emails = file_object.read()

duplicate_emails = emails.split(',')
print(duplicate_emails)

duplicate_free_emails = []

for email in duplicate_emails:
    if email not in duplicate_free_emails:
        duplicate_free_emails.append(email)

print(duplicate_free_emails)

with open("duplicate_free_emails.txt", "w") as file:
    for email in duplicate_free_emails
        file.write(email)
        file.write("\n")








content = file.read
email_dup_list.append(content)
# print (content)

for index in range(0, len(email.list))
    email = email_dup_list[index]
    print([index])
