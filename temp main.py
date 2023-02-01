from vigenere_alphabet import *

with open('text.txt', 'r') as file:
    text = file.read().rstrip('\n')

vigenere_key = input("Input your key: ")

encryptText(text, vigenere_key)   