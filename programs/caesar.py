# Andrew Zhou
# Caesar Cipher - PA Computer Science Fair

# ------ Functions ------

def caesar(text, shift, method):        # Function that encodes a message
    shifttext = []                      
    ciphertext = ""
    restricted = "0123456789!@#$%^&*()~`_-+=[]{};:\"'\|<>,./ "
    for letter in text:                 # for all letters in the plaintext

        textNum = ord(letter)           # change all letters into unicode values

        if letter in restricted:
            textNum += 0
        elif (method):
            textNum += shift
        else:
            textNum -= shift            # adds shift number to unicode value
            
        if letter.isupper():          # makes sure that the value is still a letter
            if textNum > ord('Z'):
                textNum -= 26
            elif textNum < ord('A'):
                textNum += 26
        elif letter.islower():
            if textNum > ord('z'):
                textNum -= 26
            elif textNum < ord('a'):
                textNum += 26

        shifttext.append(textNum)       # Adds values onto a list of unicode values

    for num in shifttext:               # for all numbers in the unicode value array
        letter = chr(num)               # Converts unicode back into string
        ciphertext += letter        # Adds letter into a string
            
    print("Ciphertext: " + ciphertext)  # prints string

# ------ Main Code ------

print("\t------CAESAR CIPHER------\n")

print("Are you encrypting a message or decrypting a message? (use a lowercase 'e' or 'd')")
crypto = input("Input: ")
usertext = input("Please input the text: ")                           
change = int(input("Please input the amount of shift (1 - 26): "))

if (change > 26):
    change %= 26
    
if crypto == "e":
    crypto = True
elif crypto == "d":
    crypto = False

caesar(usertext, change, crypto)
