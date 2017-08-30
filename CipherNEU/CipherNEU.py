import Cipher.Caesar
plaintext = "Hello, World!"
key = 3
print(plaintext)
ciphertext = Cipher.Caesar.Encrypt(plaintext, key)
print(ciphertext)
print(Cipher.Caesar.Decrypt(ciphertext, key))
