#GQY/Cipher/RSA
# need download lib first
# pip install rsa
# -*- coding: utf-8 -*-

import base64
import rsa

(publickey,privatekey) = rsa.newkeys(1024)

with open('public.pem','w') as f:
    f.write(publickey.save_pkcs1().decode())

with open('private.pem','w') as f:
    f.write(privatekey.save_pkcs1().decode())

with open('public.pem','r') as f:
    pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())

with open('private.pem','r') as f:
    privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())

#message = "Hello World!"

#ciphertext = rsa.encrypt(message.encode(),pubkey)

#plaintext = rsa.decrypt(ciphertext,privkey).decode() # the plaintext is bytes

#print (plaintext)

