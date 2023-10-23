#arithmitic test
import random
import time

typeQ = 0
a = 0
b = 0
c = 0
expected = 0
count_right = 0
count_wrong = 0
highscore = 0
#start
print("Hello, this is a basic arithmitic test")
name = input("Please enter your name here: ")
validate = 0
while validate != 1:
    questionnum = int(
        input(
            "Please enter the number of questions you want to answer (1-100): "
        ))
    if questionnum <= 101 and questionnum >= 1:
        validate = 1
    else:
        print("Error: please enter a valid input")
        time.sleep(0.5)
for count in range(questionnum):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    typeQ = random.randint(1, 4)
    if typeQ == 1:
        print("Addition: please add ", a, " and ", b)
        expected = a + b
        if int(input("Answer: ")) == expected:
            print("Correct")
            count_right = count_right + 1
        else:
            print("Wrong, the answer is ", expected)
            count_wrong = count_wrong + 1
    if typeQ == 2:
        print("Subtraction: please subtract ", b, " from ", a)
        expected = a - b
        if int(input("Answer: ")) == expected:
            print("Correct")
            count_right = count_right + 1
        else:
            print("Wrong, the answer is ", expected)
            count_wrong = count_wrong + 1
    if typeQ == 3:
        print("Multiplication: please multiply ", a, " and ", b)
        expected = a * b
        if int(input("Answer: ")) == expected:
            print("Correct")
            count_right = count_right + 1
        else:
            print("Wrong, the answer is ", expected)
            count_wrong = count_wrong + 1
    if typeQ == 4:
        while a % b != 0:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
        print("Division: please divide ", a, " with ", b,
              " (Only to 2 decimal places)")
        expected = round(a / b, 2)
        if float(input("Answer: ")) == expected:
            print("Correct")
            count_right = count_right + 1
        else:
            print("Wrong, the answer is ", expected)
            count_wrong = count_wrong + 1
print(name, ", you got ", count_right, " correct and ", count_wrong, " wrong")
if count_right >= highscore:
    highscore = count_right