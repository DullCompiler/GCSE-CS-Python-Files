grade = input("Enter student grade: ")
grade=int(grade)
if grade >=75:
  print(grade, " is marked as an A")
elif grade >=60 <=74:
  print(grade, " is marked as a B")
elif grade >=50 <=59:
  print(grade, " is marked as a C")
else:
  print(grade, " is makred as a F")