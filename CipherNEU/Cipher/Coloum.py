#GQY/Cipher/Column permution cipher

# define function
def TranspositionCipher(key, message):  
    """ 
    @param key: a positive number used for encryption 
    @param message: the plain text needs encryption 
    @return: the encrypted text 
    """  
    if key <= 0: # the algorithm can't work
        print("key is less than 0,can not work")
        return message   
    else:  
        return "".join([message[i::key] for i in range(key)])


def DecryptTranspositionCipher(key, message):  
    """ 
    @param key: a positive number used for encryption 
    @param message:  the encrypted message 
    @return: plaintext 
    """  
    import math  
    numOfColumns = math.ceil(len(message) / key)  
    numOfRows = key  
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
    return ''.join(plaintext)  

plaintext = input("Input the plaitext \n")
key = int(input("Input the key \n"))

# call function
Ciphertext = TranspositionCipher(key,plaintext)

print ("The Ciphertext is %s" % Ciphertext)

sResult = DecryptTranspositionCipher(key,Ciphertext)

print ("Plaintext is %s" % sResult)


