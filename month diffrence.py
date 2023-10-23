#month diffrence alert system
md=0
v_answer=0
loop=0

while loop==0:
    print("Is user behind on payments? (y/n)")
    v_answer=input()
    if v_answer=="y":
        print("how many months is the user overdue?")
        md=int(input())
        if md==3:
            print("Send an email voucher")
        elif md==6:
            print("Marked customer as lapsed")
        else:
            print("No action needed")
    elif v_answer=="n":
        print("How many months is the user underdue?")
        md=int(input())
        if md==1:
            print("Send an email invitation")
        else:
            print("No action needed")
