import string
import random

def generateRandomKey(filename):

    randomkey = []

    for i in range(100000):
        randomkey.append(random.choice(string.ascii_letters))
        i += 1
    key = "".join(randomkey)

    with open(filename, 'w') as f:
        f.write(key)

def getKey(filetext, plaintext):
    length = len(plaintext)
    f = open(filetext,"r")
    return f.read(length)