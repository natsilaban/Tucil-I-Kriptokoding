import base64

with open("testpdf.pdf", "rb") as upload:
    x = base64.b64encode(upload.read())
    text = x.decode('utf-8')

def autoKey(text, key):
    key = list(key.upper())
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return ''.join(key)

def encryptText(text, key):
    key = autoKey(text, key)
    listofText = []
    for i in range(len(text)):
        x = ((ord(text[i])) + (ord(key[i]))) % 256
        listofText.append(chr(x))
    print (''.join(listofText))

def decryptText(text, key):
    key = autoKey(text, key)
    listofText = []
    for i in range(len(text)):
        x = ((ord(text[i])) - (ord(key[i]))) % 256
        listofText.append(chr(x))
    print (''.join(listofText))

key = "abc"
encryptText(text, key)