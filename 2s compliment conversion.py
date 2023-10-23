#2s compliment pos-neg

bit4=0
bit3=0
bit2=0
bit1=0

print("Please enter the 4 bits of your positive nible")
bit4=int(input("Enter 4th Bit (left most): "))
bit3=int(input("Enter 3rd Bit (2nd to left most): "))
bit2=int(input("Enter 2nd Bit (3rd to left most): "))
bit1=int(input("Enter 1st Bit (right most): "))
if bit1+bit2+bit3+bit4>=4:
    print("error inserted digits are invalid")
else:
    bit4=1

    if bit3==0:
        bit3=1
    else:
        bit3=0

    if bit2==0:
        bit2=1
    else:
        bit2=0

    if bit1==0:
        bit1=1
    else:
        bit1=0

    #the +1
    if bit4+bit3+bit2+bit1==4:
        print("The inverted value is ", bit4, bit3, bit2, bit1)
    elif bit1!=1:
            bit1=1
            print("The inverted value is ", bit4, bit3, bit2, bit1)
    elif bit2!=1:
            bit2=1
            print("The inverted value is ", bit4, bit3, bit2, bit1)    
    else:
        if bit3!=1:
            bit3=1
            print("The inverted value is ", bit4, bit3, bit2, bit1)
