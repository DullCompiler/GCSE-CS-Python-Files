# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
# ===>  Change the identifier x to a more meaningful name
x = "y"
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# ===> Display a suitable question to the user
x=input("Do you want me to sing? y or n")
# ===> Accept the user's input (no validation required)
if (x == "y"):
    # ===> without the last -1, then it won't display the song lyrics
    for num in range(5, -1, -1):
        print (num, "green bottles sitting on the wall")
print ("Goodbye")