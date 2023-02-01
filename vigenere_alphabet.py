def alphabetOnly(text):
    textUpperCase = text.upper()
    return ''.join(i for i in textUpperCase if i.isalpha())

def autoKey(text, key):
    key = list(key.upper())
    cleanText = alphabetOnly(text)
    if len(cleanText) == len(key):
        return key
    else:
        for i in range(len(cleanText) - len(key)):
            key.append(key[i % len(key)])
    return ''.join(key)

def encryptText(text, key):
    text = alphabetOnly(text)
    key = autoKey(text, key)
    listofText = []
    for i in range(len(text)):
        x = ((ord(text[i]) - 65) + (ord(key[i]) - 65)) % 26
        listofText.append(chr(x + 65))
    return (''.join(listofText))

def decryptText(text, key):
    text = alphabetOnly(text)
    key = autoKey(text, key)
    listofText = []
    for i in range(len(text)):
        x = ((ord(text[i]) - 65) - (ord(key[i]) - 65)) % 26
        listofText.append(chr(x + 65))
    return (''.join(listofText))