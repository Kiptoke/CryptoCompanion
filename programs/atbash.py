# Andrew Zhou
# Atbash Cipher - PA Computer Science Fair

# ------ Function ------

def atbash(intext):
    inputAlpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    atbashAlpha = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
    output = ""

    for letter in intext:
        if letter in inputAlpha:
            output += atbashAlpha[inputAlpha.index(letter)]
        else:
            output += letter
            
    return output

# ------ Main Code ------

print("\t------ATBASH CIPHER------\n")

text = input("Input a text to encipher/decipher: ")

print(atbash(text))
