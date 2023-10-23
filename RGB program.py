#RGB color generator
from turtle import Screen, Turtle
loop=1
while loop==1:
    red=0
    green=0
    blue=0
    inp_loop=0

    while inp_loop==0:
        red = int(input("Input a number between 1 and 255 for red: "))
        if red<=255 or red==255:
            green = int(input("Input a number between 1 and 255 for green: "))
            if green<=255 or green==255:
                blue = int(input("Input a number between 1 and 255 for blue: "))
                if blue<=255 or blue==255:
                    print("Varaibles successfully saved")
                    inp_loop=1
                else:
                    print("Please enter a valid input")
            else:
                print("Please enter a valid input")
        else:
            print("Please enter a valid input")

    def pen_color():

        screen.bgcolor(int(red), int(green), int(blue))

    screen = Screen()
    screen.colormode(255)

    pen_color()

    pen = Turtle()

    screen.exitonclick()
