name=input("Enter your name: ")
if name=="":
    print("Name cannot be blank!")
elif len(name)<3:
    print("Name cannot be shorter than 3 letters!")
elif len(name)>20:
    print("Name cannot be longer than 20 letters")
else:
    print("All checks passed")