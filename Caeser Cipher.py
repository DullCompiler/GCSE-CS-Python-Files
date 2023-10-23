#Caeser Cipher
keyval=0

print("This program will encrypt a word in a caeser cipher key of your choice (1-26)")
inp=input("Please insert word here: ")
inp=inp.lower()

while keyval==0:
    key=int(input("Please enter the key of your desired encryption (1-26): "))
    if key>=26 or key<=0:
        print("Please enter a valid input")
    else:
        keyval=1

text = inp
s = key

def encrypt(text,s):
   result = ""
   # transverse the plain text
   for i in range(len(text)):
      char = text[i]
      # Encrypt uppercase characters in plain text
      
      if (char.isupper()):
         result += chr((ord(char) + s-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
      else:
         result += chr((ord(char) + s - 97) % 26 + 97)
      return result
#check the above function
text = inp
s = key

print ("Plain Text : ", text)
print ("Shift pattern : ", str(s))
print ("Cipher: ", encrypt(text,s))