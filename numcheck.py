# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
num = 0
vali = 0
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
while vali != 1:
    num = int(input("Please enter a number (1 ... 20): "))
    if num <=0:
        print("Input is too low")
    elif num >=21:
        print("Input is too high")
    else:
        if (num % 2 == 0):
            print (num, "even")
        if (num % 2 == 1):
            print (num, "odd")