#grade avergae calcualtor

students=0
student_count=1
current_inp=0
low=float(100)
high=float(0)
grade=float(0)

#ask for student count
print("How many students do you want to calculate for?")
students=int(input())

#start for count
for count in range (students):
    print("Please enter grade for student ", student_count)
    continue_=0
    while continue_==0:
        current_inp=int(input())
        if current_inp>=0 and current_inp<=100:
            if current_inp<=low:
                low=current_inp
            if current_inp>=high:
                high=current_inp
            grade=grade+current_inp
            student_count=student_count+1
            continue_=1
        else:
            print("Please enter an input between 0-100")

grade=float((grade/students))
print("The average grade is ", grade)
print("The lowest grade is ", low)
print("the highest grade is ", high)
