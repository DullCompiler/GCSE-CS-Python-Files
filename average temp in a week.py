#max temp program

average=0
loop=0
day=1

print("How many days do you want to find the average temperature for?")
loop=int(input())

for count in range (loop):
    print("Enter the temperature for day ", day)
    day=day+1
    temperature=int(input())
    average=average+temperature

average = round(average/7, 2)
print("The average temp was ", average, " degrees")
