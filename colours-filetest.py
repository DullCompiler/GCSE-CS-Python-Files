file = open("colours.txt", "w")
value=""
for x in range (0,3):
  value=input("Please enter a colour: ")
  file.write(value + "\n")
file.close()

file = open("colours.txt", "r")
print(file.read())
file.close