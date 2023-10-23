import time
a1=0
a2=0
a3=0
avg=0
total=0

a1=input("Insert Number One for Average: ")
a2=input("Insert Number Two for Average: ")
a3=input("Insert Number Three for Average: ")

cd=10
while cd!=0:
  print(cd)
  time.sleep(1)
  cd=cd-1
print("Lift Off!")

total=int(a1)+int(a2)+int(a3)
avg=(total/3)
print("The Average of the inputs is ",avg)