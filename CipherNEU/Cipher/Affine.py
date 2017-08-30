'''
Affine Cipher
Programmer: Ai Zhengpeng
Date: 2017-08-30
Function:
Encrypt(plaintext, key) -> ciphertext
Decrypt(ciphertext, key) -> plaintext
_ExtendedEuclid(a, m) -> a'
'''

def Encrypt(plaintext, key):
    ciphertext = ""
    for letter in plaintext:
        if letter.islower():
            ciphertext += chr((key[0] * (ord(letter) - ord('a')) + key[1]) % 26 + ord('a'))
        elif letter.isupper():
            ciphertext += chr((key[0] * (ord(letter) - ord('A')) + key[1]) % 26 + ord('A'))
        else:
            ciphertext += letter
    return ciphertext

def Decrypt(ciphertext, key):
    plaintext = ""
    for letter in ciphertext:
        if letter.islower():
            plaintext += chr((_ExtendedEuclid(key[0], 26) * (ord(letter) - ord('a') - key[1])) % 26 + ord('a'))
        elif letter.isupper():
            plaintext += chr((_ExtendedEuclid(key[0], 26) * (ord(letter) - ord('A') - key[1])) % 26 + ord('A'))
        else:
            plaintext += letter
    return plaintext

def _ExtendedEuclid(a, m):
    x1, x2, x3 = 1, 0, m
    y1, y2, y3 = 0, 1, a
    while True:
        if y3 == 0:
            return 0
        if y3 == 1:
            return y2
        q = x3 // y3
        t1, t2, t3 = x1 - q * y1, x2 - q * y2, x3 - q * y3
        x1, x2, x3 = y1, y2, y3
        y1, y2, y3 = t1, t2, t3
