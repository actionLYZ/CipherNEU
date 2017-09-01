##################################################
#未完待续, 期待李远志的新程序！（本程序函数可用）#
##################################################
'''
cipher: PlayfairCipher
Programmer: TSM
Date: 2017-08-30
Function:
Encrypt(plaintext, key)
Decrypt(ciphertext, key)  
'''
#生成加密矩阵函数
def CreateMatrix(key):
    index = 0   #keyword有效位
    for i in range(0,len(key)):
        if(key[i] == 'j'):
            key[i] = 'i'
    tempLetters = ['\0',]*25
    num = 0     #tempLetters字母个数
    encryptMatrix = [([0] * 5) for i in range(5)]
    for i in range(0,5):
        for j in range(0,5):
            if(index<len(key)):
                for k in range(index,len(key)):
                    if(key[k] in tempLetters):
                        index += 1
                    else:
                        encryptMatrix[i][j] = key[k]
                        index += 1
                        tempLetters[num] = key[k]
                        num += 1
                        break
            else:
                for k in range(0,26):
                    if(k==9):
                        continue
                    if(chr(k+97) in tempLetters):
                        continue
                    else:
                        encryptMatrix[i][j] = chr(k+97)
                        tempLetters[num] = chr(k+97)
                        num += 1
                        break
    return encryptMatrix

#判断字母是否在矩阵一行/列
def InSameRC(mode, encryptMatrix, x, y):    #mode = 0: row, mode = 1: coloum
    if(mode==0):
        for i in range(0,5):
            if((x in encryptMatrix[i])&(y in encryptMatrix[i])):
                return 1
    elif(mode==1):
        col = 0
        for i in range(0,5):
            for j in range(0,5):
                if(encryptMatrix[i][j]==x):
                    col = j
                    break
            break
        for i in range(0,5):
            if(encryptMatrix[i][col]==y):
                return 1
    return 0
#字母上/下/左/右边一位
def NextLetter(mode, encryptMatrix, x):
    for i in range(0,5):
        for j in range(0,5):
            if(encryptMatrix[i][j]==x):
                if(mode==3):
                    return encryptMatrix[i][(j+1)%5]
                elif(mode==1):
                    return encryptMatrix[(i+1)%5][j]
#找到字母行列坐标
def Position(encryptMatrix, letter):
    p = [0,0]
    for i in range(0,5):
        for j in range(0,5):
            if(encryptMatrix[i][j]==letter):
                p[0] = i
                p[1] = j
                return p
#加密函数
def Encrypt(plaintext, key):
    #生成加密矩阵
    encryptMatrix = [([0] * 5) for i in range(5)]
    encryptMatrix = CreateMatrix(key)
    #处理明文字符串
    tempPlaintext = ['\0',]*50
    tempCiphertext = ['\0',]*50
    ciphertext = ['\0',]*50
    #去掉原始明文字符串中非字母符号
    num = 0     #原始明文字符串有效字符个数
    inNum = 0   #填充无效字符个数
    for i in range(0,len(plaintext)):
        if(97<=ord(plaintext[i])<=122):  #原始明文为小写字母
            tempPlaintext[num] = plaintext[i]
            num += 1
        elif(65<=ord(plaintext[i])<=90): #原始明文为大写字母
            tempPlaintext[num] = chr(ord(plaintext[i])+32)
            num += 1
    #将有效明文中的j换成i
    for i in range(0,num):
        if(tempPlaintext[i] == 'j'):
            tempPlaintext[i] = 'i'
    #若有效明文中有相邻重复字母插入无效字符
    for i in range(0,int(num/2)):
        if(tempPlaintext[2*i]==tempPlaintext[2*i+1]):
            for j in range(0,num-2*i-1):
                tempPlaintext[num-j] = tempPlaintext[num-j-1]
            tempPlaintext[2*i+1] = 'q'  #填充无效字符q
            inNum += 1
            num += 1
    #若有效明文为基数末尾加上无效字符
    if(num%2==1):
        tempPlaintext[num] = 'q'
        inNum += 1
        num += 1
    #加密有效字符串
    for i in range(0,int(num/2)):
        if(InSameRC(0, encryptMatrix, tempPlaintext[2*i], tempPlaintext[2*i+1])==1):  #字符对在同一行
            tempCiphertext[2*i] = NextLetter(3, encryptMatrix, tempPlaintext[2*i])
            tempCiphertext[2*i+1] = NextLetter(3, encryptMatrix, tempPlaintext[2*i+1])
        elif(InSameRC(1, encryptMatrix, tempPlaintext[2*i], tempPlaintext[2*i+1])==1):    #字符对在同一列
            tempCiphertext[2*i] = NextLetter(1, encryptMatrix, tempPlaintext[2*i])
            tempCiphertext[2*i+1] = NextLetter(1, encryptMatrix, tempPlaintext[2*i+1])
        else:
            r1 = r2 = c1 = c2 = 0
            [r1,c1] = Position(encryptMatrix, tempPlaintext[2*i])
            [r2,c2] = Position(encryptMatrix, tempPlaintext[2*i+1])
            tempCiphertext[2*i] = encryptMatrix[r1][c2]
            tempCiphertext[2*i+1] = encryptMatrix[r2][c1]
    #转换密文字符串
    num = 0
    for i in range(0,len(plaintext)+inNum):
        if((97<=ord(plaintext[i])<=122)|(65<=ord(plaintext[i])<=90)):
            ciphertext[i] = tempCiphertext[num]
            num += 1
        else:
            ciphertext[i] = plaintext[i]
    ciphertext = ciphertext[:len(plaintext)]
    ciphertext = ''.join(ciphertext)
    return ciphertext

ciphertext = Encrypt("apccdefg","apple")
print(ciphertext)

