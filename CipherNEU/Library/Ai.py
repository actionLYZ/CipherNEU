'''
Ai's Library
Programmer: Ai Zhengpeng
Date: 2017-09-01
Functions:
GCD(a, b) -> b/GCD(b, a % b)
RemoveNonAlphabet(text) -> newText
IsValid(key, type) -> True/False
'''

# Calculate greatest common divisor of two integer a and b
def GCD(a, b):  
    if a % b == 0:  
        return b  
    return GCD(b, a % b)  

# Remove non-alphabet characters, such as ( ), (,), (;), etc.
def RemoveNonAlphabet(text):
    newText = ""
    for letter in text:
        if letter.isalpha():
            newText += letter
    return newText

# Check out if the key is valid, such as AES-128(16 bytes), AES-192(24 bytes), AES-256(32 bytes), etc.
def IsValid(key, type):
    if type == "Caesar":
        return isinstance(key, int) and key > 0 and key < 26
    elif ["Keyword", "Multiliteral", "Vigenere", "AutokeyCiphertext", "AutokeyPlaintext", "Playfair", "Permutation", "ColumnPermutation"].index(type) != -1:
        return isinstance(key, str) and str.isalpha()
    elif type == "Affine":
        return isinstance(key, tuple) and len(tuple) == 2 and isinstance(key[0], int) and key[0] > 0 and isinstance(key[1], int) and key[1] > 0 and GCD(key[0], key[1]) == 1
    elif type == "DoubleTransposition":
        return isinstance(key, tuple) and len(tuple) == 2 and isinstance(key[0], str) and key[0].isalpha() and isinstance(key[1], str) and key[1].isalpha()
    elif type == "RC4":
        return isinstance(key, str)
    elif type == "AES-128":
        return isinstance(key, str) and len(key) == 16
    elif type == "AES-192":
        return isinstance(key, str) and len(key) == 24
    elif type == "AES-256":
        return isinstance(key, str) and len(key) == 32
    return False

# Read bytes from the file
def FileToBytes(file):
    fin = open(file, "rb")
    text = fin.read()
    fin.close()
    return text

#Write bytes to a file
def BytesToFile(text, file):
    fout = open(file, "wb")
    fout.write(text)
    fout.close()
    return
