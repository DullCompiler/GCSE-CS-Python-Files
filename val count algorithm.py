max=0
min=100000
numval=input("How many values do you want to input: ")
count=int(numval)
while count>0:
    valinp=int(input("enter value: "))
    if valinp>max:
        max=valinp
    if valinp<min:
        min=valinp
    count=count-1
print(int(min)+int(max)/int(numval))