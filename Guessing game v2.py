#guessing game v2
import random
import time

#getting random number
number=random.randint(1,10)

#setting variables
guesses=0
finish=0
end_result=0

#intro
print("Hello, what's your name?")
name=input()
print("Hello, ", name, " welcome to the guessing game")
time.sleep(1)
print("I've chosen a number from one to ten, do you think you can guess it?")
time.sleep(1)
print("y or n")

#decision
if input()=="n":
    #user is a lazy git
    print("oh well ¯\_(ツ)_/¯")
else:
    #start
    print("great, let the game begin!")
    time.sleep(1)
    print("oh. by the way, try to get the number in 4 guesses :)")
    print("enter your guess")
    while finish!=1:
        guess=int(input())
        guesses=guesses+1
        if guesses>=4:
            print("you've had more guesses than the ideal ( 4 )")
            end_result=1
        if guess==number:
            #finish
            finish==1
            print("Well done ", name, "! You got the number (",number,") in ", guesses, " guesses")
            if end_result==1:
                time.sleep(1)
                print("you took ", (guesses-4), " more guesses than ideal :/")
        else:
            if guess>=number:
                #guess was too high
                print("guess was too high")

            if guess<=number:
                #guess was too low
                print("guess was too low")

