'''
Cipher: DH Secretkey Exchange 
Usage: secretkey exchange through multiple person
Programmer: TSM
Date: 2017-09-04
Function:
Generate(num)   input number of people and output secretkey 
'''

import random
import math

def calculatePrimitiveRoot(p):
    p -= 1
    re = p
    for i in range(2, int(math.sqrt(p)) + 1):
        if p % i == 0:
            re -= (re / i)
            while p % i == 0:
                p /= i
    if p > 1:
        re -= (re / p)
    return re

def generate():
    while True:
        p = random.randint(2, 65535)
        if isPrime(p):
            break
    g = int(calculatePrimitiveRoot(p))
    return p, g

def isPrime(num):
    if num > 1:
    # 查看因子
        for i in range(2,num):
            if (num % i) == 0:
                return False
            else:
                return True
     # 如果输入的数字小于或等于 1，不是质数
    else:
        return False

'''
import random

#定义Person类
class Person(object):
    pass

#判断质数
def IsPrime(num):
    if num > 1:
    # 查看因子
        for i in range(2,num):
            if (num % i) == 0:
                return False
            else:
                return True
     # 如果输入的数字小于或等于 1，不是质数
    else:
        return False

#生成DH密钥函数
def Generate(num):
    #print("------3 People Exchange SecretKey------")
    while(1):
        p = random.randint(1000,5000)
        if(IsPrime(p)):
            break
    g = random.randint(0,p)
    objs = []
    #生成Person实例列表
    for i in range(0,num):
        obj = Person()
        objs.append(obj)
    L = random.sample([i for i in range(100)],num)
    #print("Each person choose a secret number:")
    for i in range(0,num):
        objs[i].secNum = L[i]
        #print(chr(65+i),end=': ')
        #print(objs[i].secNum)
        objs[i].known = pow(g,L[i]) % p
    #print("----------------------------------")
    for i in range(0,num-1):
        #print("Round",end=' ')
        #print(i+1)
        for j in range(0,num):
            objs[j].get = objs[j-1].known
        for j in range(0,num):
            objs[j].known = pow(objs[j].get,objs[j].secNum)%p
            #print(chr(65+j),end=': ')
            #print(objs[j].known)
        #print("----------------------------------")
    return objs[0].known

#测试数据
#a = Generate(3)
#print("Final Secretkey:",end=' ')
#print(a)
'''
