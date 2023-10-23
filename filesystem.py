import platform 

print("filesys initialising")

loop = 0
choice = ""
value = ""


def a(value):
    file = open("filesystem.txt", "w")
    for x in range(0, 5):
        value = input(
            "Please enter data to enter into new list (five enteries) : ")
        file.write(value + "\n")
    file.close()


def b(value):
    file = open("filesystem.txt", "a")
    for x in range(0, 5):
        value = input(
            "please enter data to append into the file (five enteries) : ")
        file.write(value + "\n")
    file.close()


def c():
    file = open("filesystem.txt", "r")
    print(file.read())
    file.close()

def d():
    print("This is a diagnostic panel")
    print("Showing System Specs")
    my_system = platform.uname()
    print(f"System: {my_system.system}")
    print(f"Node Name: {my_system.node}")
    print(f"Release: {my_system.release}")
    print(f"Version: {my_system.version}")
    print(f"Machine: {my_system.machine}")
    print(f"Processor: {my_system.processor}")
    print("These are not the droids you're looking for")


def e():
    print("stopping service: filesystem.py")


while loop != 1:
    print("a) Create new list")
    print("b) Add data to existing list")
    print("c) Display data")
    print("d) System Specifications")
    print("e) Quit")

    choice = input("Enter choice here: ")
    if choice == "a":
        a(value)

    if choice == "b":
        b(value)

    if choice == "c":
        c()

    if choice == "d":
        d()
	
    if choice == "e":
        e()
        loop = 1