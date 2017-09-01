from Cipher.PlayFair  import*
str = "hello world! today is a good day!"
key = "hello"
a = makeKeyList(key)
for list in a:
    print(list)
cipherText = (Encrypt(str,key))
print(cipherText)
plainText = (Decrypt(cipherText,key))
print(plainText)
