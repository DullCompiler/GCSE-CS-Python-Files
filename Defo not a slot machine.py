import random

rolls=["Cherry", "Bell", "Lemon", "Orange", "Skull", "Star"]

credit=1

loop=0
roll1=0
roll2=0
roll3=0
while loop==0:
    if input("Would you like to roll (y or n) ")=="y":
        credit = credit - 0.2
        roll1=random.randint(0,5)
        print("Your first roll was ", rolls[roll1])
        roll2=random.randint(0,5)
        print("Your second roll was ", rolls[roll2])
        roll3=random.randint(0,5)
        print("Your third roll was ", rolls[roll3])
    
        if roll1 == roll2  or roll2 == roll3 or roll3 == roll1:
            print("Well done! you got two matches! You won 50p")
            credit = credit + 0.5  
        elif roll1 == roll2  and  roll1 == roll3:
            print("Well done! You got 3 Jackpot! 1 Pound added to your account")
            credit = credit + 1
        else:
            print("You didn't win anyhting, best try again")
        print("Your credit is : ", round(credit, 2))

    else:
        print("Oh well")
        loop=1
