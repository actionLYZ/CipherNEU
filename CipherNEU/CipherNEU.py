import Cipher.Affine
plaintext = "hot"
key = (7, 3)
print(plaintext)
ciphertext = Cipher.Affine.Encrypt(plaintext, key)
print(ciphertext)
print(Cipher.Affine.Decrypt(ciphertext, key))
