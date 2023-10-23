god_help_me=0
while god_help_me==0:
    validanswer=0
    validanswer2=0

    bits=[]
    bita1=0
    bitb1=0
    bitc1=0
    bitd1=0

    bits2=[]
    bita2=0
    bitb2=0
    bitc2=0
    bitd4=0

    answer=0

    sumb=0
    
    print("Getting nible one")
    while validanswer==0:
        print("Please enter your bits (left to right)")
        bita1=int(input())
        bitb1=int(input())
        bitc1=int(input())
        bitd1=int(input())
        if bita1+bitb1+bitc1+bitd1>=5:
            print("Please enter a valid input range")
        else:
            validanswer=1

    print("Getting nible two")
    while validanswer2==0:
        print("Please enter your bits (left to right)")
        bita2=int(input())
        bitb2=int(input())
        bitc2=int(input())
        bitd2=int(input())
        if bita2+bitb2+bitc2+bitd2>=5:
            print("Please enter a valid input range")
        else:
            validanswer2=1
