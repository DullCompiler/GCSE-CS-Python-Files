#denary to hexidecimal
choice=0
loop2=1
loop3=1

print("Do you want to convert denary to hexadecimal (a)")
print("Do you want to convert binary to hexadecimal (b)")
choice=input("a or b : ")
if choice=="a":
    loop2=0
elif choice=="b":
    loop3=0

#denary to hexadecimal
while loop2==0:
    loop1=0
    oriinp=0
    hex_1=0
    hex_2=0
    hex_full=[]

    print("Please enter a valid input (0-255)")
    while loop1==0:
        oriinp=int(input())
        if oriinp<=255 and oriinp>=0:
            loop1=1
        else:
            print("input not valid please try again")

    hex_1=int((oriinp)//(16))
    hex_2=int(oriinp-(hex_1*16))
    #print(hex_1)
    #print(hex_2)

    if hex_1==10:
        hex_1="A"
    if hex_1==11:
        hex_1="B"
    if hex_1==12:
        hex_1="C"
    if hex_1==13:
        hex_1="D"
    if hex_1==14:
        hex_1="E"
    if hex_1==15:
        hex_1="F"

    if hex_2==10:
        hex_2="A"
    if hex_2==11:
        hex_2="B"
    if hex_2==12:
        hex_2="C"
    if hex_2==13:
        hex_2="D"
    if hex_2==14:
        hex_2="E"
    if hex_2==15:
        hex_2="F"

    hex_full=[hex_1, hex_2]
    print("The hexidecimal is ", hex_full)

#binary to hexidecimal
while loop3==0:
    loop1=0
    oribin=[]
    oriinp=0
    hex_1=0
    hex_2=0
    hex_full=[]

    print("Please enter your 8 bit binary string")
    print("Please enter one digit at a time")
    for count in range (8):
        oriinp=int(input())
        if oriinp==1 or oriinp==0:
            oribin.append(oriinp)
        else:
            print("input not valid please try again")

    print("Binary input is ", [oribin], "Commencing conversion")

    length=len(oribin)
    middle_index=length//2
    first_half=oribin[:middle_index]
    second_half=oribin[middle_index:]

    if first_half=="0000":
        hex_1="0"
    if first_half=="0001":
        hex_1="1"
    if first_half=="0010":
        hex_1="2"
    if first_half=="0011":
        hex_1="3"
    if first_half=="0100":
        hex_1="4"
    if first_half=="0101":
        hex_1="5"
    if first_half=="0110":
        hex_1="6"
    if first_half=="0111":
        hex_1="7"
    if first_half=="1000":
        hex_1="8"
    if first_half=="1001":
        hex_1="9"
    if first_half=="1010":
        hex_1="A"
    if first_half=="1011":
        hex_1="B"
    if first_half=="1100":
        hex_1="C"
    if first_half=="1101":
        hex_1="D"
    if first_half=="1110":
        hex_1="E"
    if first_half=="1111":
        hex_1="F"

    if second_half=="0000":
        hex_2="0"
    if second_half=="0001":
        hex_2="1"
    if second_half=="0010":
        hex_2="2"
    if second_half=="0011":
        hex_2="3"
    if second_half=="0100":
        hex_2="4"
    if second_half=="0101":
        hex_2="5"
    if second_half=="0110":
        hex_2="6"
    if second_half=="0111":
        hex_2="7"
    if second_half=="1000":
        hex_2="8"
    if second_half=="1001":
        hex_2="9"
    if second_half=="1010":
        hex_2="A"
    if second_half=="1011":
        hex_2="B"
    if second_half=="1100":
        hex_2="C"
    if second_half=="1101":
        hex_2="D"
    if second_half=="1110":
        hex_2="E"
    if second_half=="1111":
        hex_2="F"

    hex_full=[hex_1, hex_2]
    print("The hexidecimal is ", hex_full)

