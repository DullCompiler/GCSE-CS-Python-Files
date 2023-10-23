#Library Book Counter
print("Welcome to the student reading tracker")

#vars
names=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
books=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lowten=[0]
highest_books=0
highest_name=0
highest_books2=0
highest_name2=0
highest_books3=0
highest_name3=0
validate=0

#input
countsys=0
for count in range (10):
    names[(countsys)]=str(input("Please enter the name of the student "))
    while validate==0:
        books[(countsys)]=int(input("Please enter the nunber of books read by the student "))
        if books[countsys]<=100 or books[countsys]==100 and books[countsys]>=0:
            validate=1
        else:
            print("Please enter a valid input (0-100)")
    if books[countsys]<=10:
        lowten.append(names[countsys])

    if books[countsys]>=highest_books:
        highest_books2=highest_books3
        highest_name2=highest_books3
        highest_books=highest_books2
        highest_name=highest_name2
        highest_books=books[countsys]
        highest_name=names[countsys]
    countsys=countsys+1
    validate=0

#results
countsys=0
for count in range (10):
    print(names[countsys], ", read ", books[countsys])
    countsys=countsys+1
print("The most books read was ", highest_books, " by ", highest_name)
print("The second most books read was ", highest_books2, " by ", highest_name2)
print("The thrid most books read was ", highest_books3, " by ", highest_name3)
print("These people read below ten books", lowten)
