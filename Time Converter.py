#Time converter

hour=0
minutes=0
time=0
validation=0
m_valid=0
h_valid=0

while validation==0:
    while h_valid==0:
        hour=int(input("Enter the 24 hour format hour (0-23): "))
        if hour<=24:
            h_valid=1

    while m_valid==0:
        minutes=int(input("Enter the 24 hour format minutes (0-59): "))
        if minutes<=60:
            m_valid=1

    if hour<12:
        time="am"
    else:
        time="pm"
        hour=hour-12

    print("The time is ", hour, ": ", minutes, " ", time)
    m_valid=0
    h_valid=0
    print("Do you want to repeat code? (y/n)")
    answer=input()
    if answer=="n":
        validation=1
        print("valid input")
    elif answer=="y":
        print("valid input")
    else:
        print("error, repeat input invalid - repeating anyways")
