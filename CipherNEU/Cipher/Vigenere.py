'''
cipher: VigenereCipher
Programmer: TSM
Date: 2017-08-30
Function:
Encrypt(plaintext, key)
Decrypt(ciphertext, key)  
'''
#加密函数
def Encrypt(plaintext, key):
    ciphertext = ['\0',]*50
    tempPlaintext = ['\0',]*50
    tempCiphertext = ['\0',]*50
    #建立Vigenere Table
    table = [([0] * 26) for i in range(26)]
    for i in range(0,26):
        for j in range(0,26):
            table[i][j] = (i+j)%26
    #处理原始明文字符串
    num = 0;    #有效明文字数
    for i in range(0,len(plaintext)):
        if(97<=ord(plaintext[i])<=122):  #原始明文为小写字母
            tempPlaintext[num] = plaintext[i]
            num += 1
        elif(65<=ord(plaintext[i])<=90): #原始明文为大写字母
            tempPlaintext[num] = chr(ord(plaintext[i])+32)
            num += 1
    #有效明文字符串转换为密文
    for i in range(0,num):
        tempCiphertext[i] = chr(table[ord(key[i%len(key)])-97][ord(tempPlaintext[i])-97]+97)
        print(tempCiphertext[i],end=' ')
    #转换密文字符串
    for i in range(0,len(plaintext)):
        if((97<=ord(plaintext[i])<=122)|(65<=ord(plaintext[i])<=90)):
            ciphertext[i] = tempCiphertext[i]
        else:
            ciphertext[i] = plaintext[i]
    print(ciphertext)
    ciphertext = ciphertext[:len(plaintext)]
    ciphertext = ''.join(ciphertext)
    return ciphertext

ciphertext = Encrypt("dfaf asd","cds")
print(ciphertext)



