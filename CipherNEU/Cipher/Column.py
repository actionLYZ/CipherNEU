#GQY/Cipher/Column permution cipher (include double)

# -*- coding: utf-8 -*-

# define function

import os

str = "abcdefghijklmnopqrstuvwxyz"

def Encrypt_Col(key,message):

    key = key.lower()
    key1 = [0]
    for i in range(len(key) - 1):
        key1.append(0)

    tmp = 0
    for i in range(26):
        for j in range(len(key)):
            if (str[i] == key[j]):
                key1[j] = i + tmp + 1
                tmp += 1
        tmp = 0

    if len(key) <= 0: # the algorithm can't work
        print("key is less than 0,can not work")
        return message   
    else:  
        return "".join([message[i-1::len(key)] for i in key1]) #return the ciphertext


def Decrypt_Col(key,message):  
    key = key.lower()
    key1 = [0]
    key2 = [0]
    for i in range(len(key) - 1):
        key1.append(0)
        key2.append(0)

    tmp = 0
    for i in range(26):
        for j in range(len(key)):
            if (str[i] == key[j]):
                key1[j] = i + tmp + 1
                tmp += 1
        tmp = 0
        
    for i in range(len(key)): #do not forget plus 1
        for j in range(len(key)):
            if ((i+1) == key1[j]):
                key2[i] = j + 1
    

    sResult = ""

    import math  
    numOfColumns = math.ceil(len(message) / len(key))  
    numOfRows = len(key)  
    numOfShadeBoxes = (numOfColumns * numOfRows) - len(message)  
    plaintext = [''] * numOfColumns  
     
    col = 0  
    row = 0  
    for symbol in message:  
        plaintext[col] += symbol  
        col += 1  
      
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadeBoxes):  
            col = 0  
            row += 1
    tmp = ''.join(plaintext)

    for i in range(numOfColumns):
        for j in key2:
            if ((i*row + j - 1)<(len(tmp))):
                sResult += tmp[i*row + j - 1]
                #print (tmp[i*row + j - 1])

    print ("---------------")
    return sResult
    #return ''.join(plaintext)  

# call function
#plaintext = input("Input the plaitext \n")
#key = input("Input the key \n")

Ciphertext = Encrypt_Col(key,plaintext)

print ("The Ciphertext is %s" % Ciphertext)

sResult = Decrypt_Col(key,Ciphertext)

print ("Plaintext is %s" % sResult)
