#Convert to binary

#forever loop
loop=1
while loop==1:

    #variables
    inp_loop=0
    answer=["0", "0", "0", "0", "0", "0", "0", "0"]

    #input
    print("Welcome to the Denerary to binary converter")
    while inp_loop==0:
        inp=int(input("Please enter a number that is within 0-255 "))
        if 0 <= inp <= 255:
            inp_loop=1
        else:
            print("Please enter a valid input")

    #Testing

    if inp>128 or inp==128:
        (answer[0])="1"
        inp=inp-128

    if inp>64 or inp==64:
        (answer[1])="1"
        inp=inp-64

    if inp>32 or inp==32:
        (answer[2])="1"
        inp=inp-32

    if inp>16 or inp==16:
        (answer[3])="1"
        inp=inp-16

    if inp>8 or inp==8:
        (answer[4])="1"
        inp=inp-8

    if inp>4 or inp==4:
        (answer[5])="1"
        inp=inp-4

    if inp>2 or inp==2:
        (answer[6])="1"
        inp=inp-2

    if inp==1:
        (answer[7])="1"
        inp=inp-1

    print(answer)
