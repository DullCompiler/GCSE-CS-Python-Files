import time
num=0
while num<=100:
    if (num%5==0) and (num%3==0):
        #print(num, "is divisble by 3 and 5")
        print("FizzBuzz")
    elif num%5==0:
        #print(num, " is divisble by 5")
        print("Buzz")
    elif num%3==0:
        #print(num, " is divisble by 3")
        print("Fizz")
    else:
        print(num)
    time.sleep(0.5)
    num = num+1