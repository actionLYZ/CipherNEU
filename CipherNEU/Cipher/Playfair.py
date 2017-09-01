'''
Name: Playfair Cipher
Programmer: AI
Date: 2017-09-01
State: alpha
Note: Remove punctuations and change all upper letters to lower case.
Example:

import Cipher.Playfair
p = "speciallity"
k = "harpsichord"
c = Cipher.Playfair.Encrypt(p, k)
print(c)
print(Cipher.Playfair.Decrypt(c, k))

'''

def Encrypt(plaintext, key):
    ciphertext = ""
    table = _CreateMatrix(key)
    newPlaintext = _SortOutText(plaintext)
    for i in range(0, len(newPlaintext), 2):
        if table.find(newPlaintext[i]) // 5 == table.find(newPlaintext[i + 1]) // 5:
            ciphertext += table[table.find(newPlaintext[i]) // 5 * 5 + (table.find(newPlaintext[i]) % 5 + 1) % 5]
            ciphertext += table[table.find(newPlaintext[i + 1]) // 5 * 5 + (table.find(newPlaintext[i + 1]) % 5 + 1) % 5]
        elif table.find(newPlaintext[i]) % 5 == table.find(newPlaintext[i + 1]) % 5:
            ciphertext += table[(table.find(newPlaintext[i]) // 5 + 1) % 5 * 5 + table.find(newPlaintext[i]) % 5]
            ciphertext += table[(table.find(newPlaintext[i + 1]) // 5 + 1) % 5 * 5 + table.find(newPlaintext[i + 1]) % 5]
        else:
            ciphertext += table[table.find(newPlaintext[i]) // 5 * 5 + table.find(newPlaintext[i + 1]) % 5]
            ciphertext += table[table.find(newPlaintext[i + 1]) // 5 * 5 + table.find(newPlaintext[i]) % 5]
    return ciphertext

def Decrypt(ciphertext, key):
    plaintext = ""
    table = _CreateMatrix(key)
    for i in range(0, len(ciphertext), 2):
        if table.find(ciphertext[i]) // 5 == table.find(ciphertext[i + 1]) // 5:
            plaintext += table[table.find(ciphertext[i]) // 5 * 5 + (table.find(ciphertext[i]) % 5 + 4) % 5]
            plaintext += table[table.find(ciphertext[i + 1]) // 5 * 5 + (table.find(ciphertext[i + 1]) % 5 + 4) % 5]
        elif table.find(ciphertext[i]) % 5 == table.find(ciphertext[i + 1]) % 5:
            plaintext += table[(table.find(ciphertext[i]) // 5 + 4) % 5 * 5 + table.find(ciphertext[i]) % 5]
            plaintext += table[(table.find(ciphertext[i + 1]) // 5 + 4) % 5 * 5 + table.find(ciphertext[i + 1]) % 5]
        else:
            plaintext += table[table.find(ciphertext[i]) // 5 * 5 + table.find(ciphertext[i + 1]) % 5]
            plaintext += table[table.find(ciphertext[i + 1]) // 5 * 5 + table.find(ciphertext[i]) % 5]
    return plaintext

def _CreateMatrix(key):
    table = ""
    for letter in key:
        if letter.isalpha():
            if letter.lower() == 'j':
                if table.find('i') == -1:
                    table += 'i'
            else:
                if table.find(letter.lower()) == -1:
                    table += letter.lower()
    for i in range(ord('a'), ord('z') + 1):
        if i != ord('j') and table.find(chr(i)) == -1:
            table += chr(i)
    return table

def _SortOutText(text):
    newText = ""
    for letter in text:
        if letter.isalpha():
            newText += letter.lower()
    newText2 = ""
    i = 0
    while i < len(newText):
        if i + 1 == len(newText) or newText[i] == newText[i + 1]:
            newText2 += newText[i]
            if newText[i] == 'q':
                newText2 += 'x'
            else:
                newText2 += 'q'
            i -= 1
        else:
            newText2 += newText[i]
            newText2 += newText[i + 1]
        i += 2
    return newText2
