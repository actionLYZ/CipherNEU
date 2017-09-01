'''
Ai's Library
Programmer: Ai Zhengpeng
Date: 2017-09-01
Functions:
RemoveNonAlphabet(text) -> newText
'''

# Remove non-alphabet characters, such as ( ), (,), (;), etc.
def RemoveNonAlphabet(text):
    newText = ""
    for letter in text:
        if letter.isalpha():
            newText += letter
    return newText
