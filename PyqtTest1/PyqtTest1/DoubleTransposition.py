'''
Name: Double Transposition Cipher
Programmer: AI
Date: 2017-09-01
State: alpha
Note: 
Example:

import Cipher.DoubleTransposition
p = "usingaciphertwicemayimprovethestreangthofthecipherefficiently"
k = ("what", "next")
c = Cipher.DoubleTransposition.Encrypt(p, k)
print(c)
print(Cipher.DoubleTransposition.Decrypt(c, k))

'''

import ColumnPermutation

def Encrypt(plaintext, key):
    newKey = key[0]
    newCiphertext = Cipher.ColumnPermutation.Encrypt(plaintext, newKey)
    newKey = key[1]
    ciphertext = Cipher.ColumnPermutation.Encrypt(newCiphertext, newKey)
    return ciphertext

def Decrypt(ciphertext, key):
    newKey = key[1]
    newPlaintext = Cipher.ColumnPermutation.Decrypt(ciphertext, newKey)
    newKey = key[0]
    plaintext = Cipher.ColumnPermutation.Decrypt(newPlaintext, newKey)
    return plaintext
