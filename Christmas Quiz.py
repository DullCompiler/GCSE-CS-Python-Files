#Christmas Quiz

q=["Who Santa Clause also known as? a: Saint Nick, b: fat red man, c: Elf owner", "Which Company made Santa clause famous? a: Lego, b: Coke-a-Cola, C: Tesco", "What name is one of Santa's Reindeer? a: Epstein, b: saint dick, c: Rudolph"]
a=["a", "b", "c"]
count=0
point=0

print("This is the Christmas Quiz, you will be answering 3 questions based around christmas")
print("Would you like to play?")
if input("answer y or n: ")=="y":
    while count!=3:
        print("Question", q[count])
        if input("Please enter answer here: ")==(a[count]):
            print("Correct! well done")
            point=point+1
        else:
            print("Sorry you got it wrong the answer was ", (a[count]))
        count=count+1

    print("Thanks for playing, you got ", point, " out of 3")
else:
    print("Oh Well")