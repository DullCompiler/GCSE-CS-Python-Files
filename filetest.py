file = open("file-test.txt","w")
file.write("line one\n")
file.write("line two\n")
file.write("line three\n")
file.write("line four\n")
file.close()

file = open("file-test.txt","r")
print(file.read())
file.close()