#compare
compare = int(10)

#item one
print("PLease input item one's price")
item_one=float(input())

#item two
print("PLease input item two's price")
item_two=float(input())

total=item_one+item_two

if total>=compare:
    print("sorry too much, that's ", total)
else:
    print("thats's fine, that's ", total)
