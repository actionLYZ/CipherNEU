#GQY/Cipher/Column permution cipher

# define function
def TranspositionCipher(key, message):  

    if key <= 0: # the algorithm can't work
        print("key is less than 0,can not work")
        return message   
<<<<<<< HEAD
    else:  
        # ���ؼ��ܺ������
=======
    else: 
        # 返回加密后的密文 
>>>>>>> 9ead0da96ac70b1179034d68f0183e54a16c5eeb
        return "".join([message[i::key] for i in range(key)])


def DecryptTranspositionCipher(key, message):  

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
<<<<<<< HEAD
            row += 1  
    # ���ؽ��ܺ������
=======
            row += 1
    # 返回解密后的明文  
>>>>>>> 9ead0da96ac70b1179034d68f0183e54a16c5eeb
    return ''.join(plaintext)  

plaintext = input("Input the plaitext \n")
key = int(input("Input the key \n"))

# call function
# 列置换加密
Ciphertext = TranspositionCipher(key,plaintext)

print ("The Ciphertext is %s" % Ciphertext)

sResult = DecryptTranspositionCipher(key,Ciphertext)

print ("Plaintext is %s" % sResult)

<<<<<<< HEAD
#GQY/Cipher/Column permution cipher

# define function
def TranspositionCipher(key, message):  

    if key <= 0: # the algorithm can't work
        print("key is less than 0,can not work")
        return message   
    else:  
        # ���ؼ��ܺ������
        return "".join([message[i::key] for i in range(key)])


def DecryptTranspositionCipher(key, message):  
 
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
    # ���ؽ��ܺ������
    return ''.join(plaintext)  

plaintext = input("Input the plaitext \n")
key = int(input("Input the key \n"))

# call function
Ciphertext = TranspositionCipher(key,plaintext)

print ("The Ciphertext is %s" % Ciphertext)

sResult = DecryptTranspositionCipher(key,Ciphertext)
=======
>>>>>>> 9ead0da96ac70b1179034d68f0183e54a16c5eeb

