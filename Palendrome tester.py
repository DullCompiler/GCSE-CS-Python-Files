#palindrome tester
a=0
while a==0:
    print("This program will test to see if the inputed word is a pallendrome")
    inp=input("Please insert word here: ")
    inp=inp.lower()
    palendrome_test=inp[::-1]

    if inp==palendrome_test:
        print(inp, "is a palendrome")
    else:
        print(inp, "is not a palendrome")

    #print(inp)
    #print(palendrome_test)
    #print(length)

