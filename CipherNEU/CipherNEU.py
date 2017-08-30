import Cipher.Keyword
plaintext = "Hello, World!"
key = "success"
print(plaintext)
ciphertext = Cipher.Keyword.Encrypt(plaintext, key)
print(ciphertext)
print(Cipher.Keyword.Decrypt(ciphertext, key))
