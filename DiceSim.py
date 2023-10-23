import random
print("Dice Simulator")
c=1
cl=1
inp=""
while c==1:
  c=1
  cl=1
  print("Your die rolled a ",(random.randint(1,6)))
  while cl==1:
    inp = input("Do you want to roll again? y or n : ")
    if inp == "n":
      c=0
      cl=0
      print("Thanks for using Dice Simulator 2021")
    elif inp == "y":
      cl=0
    else:
      print("Invalid input")