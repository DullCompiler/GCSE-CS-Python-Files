#16/4/2021
#Challenge 1

name = ""
colour = ""


def one(name):
    print("Hello, what's your name?")
    name = input("Please enter your name here: ")
    print("Hello ", name)


def two(colour, name):
    print(name, " what is your favorite colour?")
    colour = input("Please enter the colour here: ")
    print("I like ", colour, " too!")


def three():
    print("Goodbye!")


while 0 + 0 == 0:

    print("Enter a number between 1-3")
    if input() == "1":
        one(name)
    if input() == "2":
        two(colour, name)
    if input() == "3"
        three()