error = open("emailerror.txt","w")
email = open("emails.txt","r")

with open("emails.txt") as email.readlines:
  for line in email:
    if "@" not in line:
      error.write(line)

error.close()
email.close()

print("Task Completed Succesfully")