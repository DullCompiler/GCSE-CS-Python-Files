print("Trinagle area calculator")
print("Formula = 0.5 x Base x Perp Height")
print("or 0.5 * a * b")

a = 0.0
b = 0.0
ans = 0.0
val = 0

while val == 0:
    a = input("What is your base?: ")
    b = input("What is your perpendicular height: ")
    print("Processing Inputs")
    if float(a) >= 0 and float(b) >= 0:
        val = 1
        print("succesfully noted inputs, proceding")
    else:
        print("error#01")
        print("Task failed succesfully, please enter valid inputs (1+)")

ans = ((float(a) * float(b))/2)
print("The area of the triangle is : ", ans)