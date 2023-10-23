from turtle import *
a=2
b=0.1
for i in range(1000):
    width(6)
    left(33+a)
    forward(b)
    right(90)
    forward(b)
    speed(0)
    a=a+2
    b=b+0.1
    print(a)
    print(b)

    
