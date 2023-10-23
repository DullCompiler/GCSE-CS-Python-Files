highscore = [0,0,0,0,0,0,0,0,0,0]
for count in range (10):
    print(highscore[count])
for count in range (10):
    highscore[count] = input("Please enter a score: ")
for count in range (10):
    print("Highscore number: ", (count+1), " equals: ", highscore[count])


