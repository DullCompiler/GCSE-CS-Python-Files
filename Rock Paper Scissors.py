#rock paper scissors program
import time
import random

#variables
p1=0
p2=0
gamecount_end=0

#intro
print("Welcome to Rock Paper Scissors")
time.sleep(1)
print("Do you want to play against the computer or watch a virtual match?")
time.sleep(1)
print("1 for Player vs Computer")
print("2 for Computer vs Computer")
choice=int(input("Please enter choice (1 or 2) : "))
#PVC
if choice==1:
    print("How many games do you want to Play?")
    gamecount=int(input())
    for count in range (gamecount):
        input_loop=0
        while input_loop==0:
            player_choice=input("r = Rock, p = Paper, s = Scissors ")
            if player_choice=="r" or player_choice=="R" or player_choice=="p" or player_choice=="P" or player_choice=="s" or player_choice=="S":
                input_loop=1
            else:
                print("Please enter a valid input")
        #Player choice
        if player_choice == "r" or player_choice=="R":
            player_choice="Rock"
        if player_choice == "p" or player_choice=="P":
            player_choice="Paper"
        if player_choice == "s" or player_choice=="S":
            player_choice="Scissors"
        #Computer two choice
        computer_two_choice=random.randint(1, 3)
        if computer_two_choice == 1:
            computer_two_choice="Rock"
        if computer_two_choice == 2:
            computer_two_choice="Paper"
        if computer_two_choice == 3:
            computer_two_choice="Scissors"
        time.sleep(1)
        print("You chose ", player_choice)
        time.sleep(1)
        print("Computer chose ", computer_two_choice)
        time.sleep(1)
        #draw
        if computer_two_choice==player_choice:
            print("You drew, no one won!")
        #rock and paper
        if computer_two_choice=='Rock' and player_choice=="Paper":
            print("You won!")
            p1=p1+1
        if player_choice=='Rock' and computer_two_choice=="Paper":
            print("Computer won!")
            p2=p2+1
        #rock and scissors
        if computer_two_choice=='Rock' and player_choice=="Scissors":
            print("Computer won!")
            p2=p2+1
        if player_choice=='Rock' and computer_two_choice=="Scissors":
            print("You won!")
            p1=p1+1
        #scissors and paper
        if computer_two_choice=='Scissors' and player_choice=="Paper":
            print("Computer won!")
            p2=p2+1
        if player_choice=='Scissors' and computer_two_choice=="Paper":
            print("You won!")
            p1=p1+1
        gamecount_end=gamecount_end+1
        if gamecount_end==gamecount:
            print("You got ", p1, " points")
            print("The Computer got ", p2, " points")
            if p1>p2:
                print("You won!")
            if p2>p1:
                print("The computer won!")
            if p1==p2:
                print("You both drew")
#CVC
if choice==2:
    print("How many games do you want to watch?")
    gamecount=int(input())
    for count in range (gamecount):
        computer_one_choice=random.randint(1, 3)
        #Computer one choice
        if computer_one_choice == 1:
            computer_one_choice="Rock"
        if computer_one_choice == 2:
            computer_one_choice="Paper"
        if computer_one_choice == 3:
            computer_one_choice="Scissors"
        #Computer two choice
        computer_two_choice=random.randint(1, 3)
        if computer_two_choice == 1:
            computer_two_choice="Rock"
        if computer_two_choice == 2:
            computer_two_choice="Paper"
        if computer_two_choice == 3:
            computer_two_choice="Scissors"
        time.sleep(1)
        print("Player One chose ", computer_one_choice)
        time.sleep(1)
        print("Player Two chose ", computer_two_choice)
        time.sleep(1)
        #draw
        if computer_two_choice==computer_one_choice:
            print("They drew, no one won!")
        #rock and paper
        if computer_two_choice=='Rock' and computer_one_choice=="Paper":
            print("Player One won!")
            p1=p1+1
        if computer_one_choice=='Rock' and computer_two_choice=="Paper":
            print("Player Two won!")
            p2=p2+1
        #rock and scissors
        if computer_two_choice=='Rock' and computer_one_choice=="Scissors":
            print("Player Two won!")
            p2=p2+1
        if computer_one_choice=='Rock' and computer_two_choice=="Scissors":
            print("Player One won!")
            p1=p1+1
        #scissors and paper
        if computer_two_choice=='Scissors' and computer_one_choice=="Paper":
            print("Player Two won!")
            p2=p2+1
        if computer_one_choice=='Scissors' and computer_two_choice=="Paper":
            print("Player One won!")
            p1=p1+1
        gamecount_end=gamecount_end+1
        if gamecount_end==gamecount:
            print("Computer one got ", p1, " points")
            print("Computer two got ", p2, " points")
            if p1>p2:
                print("Computer one won!")
            if p2>p1:
                print("Computer two won!")
            if p1==p2:
                print("They both drew")
