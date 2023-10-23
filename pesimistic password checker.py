#Aggresive Password Checker
import random
import time

insults=["A brainless chicken could do better", "Is that really all you've got?", "Try again, or stop wasting my time", "Wow, you're data must be sooooo safe, not.", "People like you are why data breaches are commonplace", "at this point you may as well just put Qwerty123", "I could do this in my sleep", "Are you stupid or are you a moron having a good day?", "Jeez, what are you eighty eight", "Why have I been brought into this world only to suffer at the literary braindeath that is that password!", "Maybe just don't use the internet"]

loop=0
passwrd_pass=0
confirm=0
valid=0
found_num=0
founf_unique_char=0


print("Hello and welcome to the Pesimistic Password Checker, this helpful program is designed to assist you in making more secure passwords")
time.sleep(1)
print("Do you want to continue? y or n")
confirm=str(input("Please enter input here : "))
while loop==0:
    if confirm=="y":
        passwrd_pass=1
        loop=1
        valid=1
    if confirm=="n":
        print("Alright then, please reconsider this service in future")
        loop=1
        valid=1
    if valid==0:
        print("Can you please enter a valid input and stop wasting my time!")

if passwrd_pass==1:
    print("Great!, how many passwords do you want to check?")
    loopfor=int(input())
    for count in range (loopfor):
        print("Please enter a password")
        password=str(input())

        chars = set('0123456789,')
        found_num=0
        if any((c in chars) for c in password):
            found_num=1

        chars = set('@#$%^&*(),[]{}\|;<>./?')
        found_unique_char=0
        if any((c in chars) for c in password):
            found_unique_char=1

        if len(password)<=30:
            insult_chosen=int(random.randint(0, 10))
            print(insults[insult_chosen])
            time.sleep(1)

            if found_unique_char==1:
                print("At least you used a unique character")
            else:
                print("You didn't even use a unique character, how lazy are you")
            time.sleep(1)

            if found_num==1:
                print("At least you used a number")
            else:
                print("You didn't even use a number, how lazy are you")
            time.sleep(1)
        
        else:
            print("Please give your keyboard a break and actually try")
            time.sleep(1)
