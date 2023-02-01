
def createKeyTable(key):
    letters = []
    for i in key:
        if i not in letters:
            if i != 'j':
                letters.append(i)

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in alphabet:
        if i not in letters:
            letters.append(i)

    matrix = []
    while letters != []:
        matrix.append(letters[:5])
        letters = letters[5:]

    return matrix

def ubahPlaintext(plaintext):
    newText = []
    n = 0
    for i in plaintext:
        if i == 'j':
            i = 'i'
        if n != 0:
            if plaintext[n] == plaintext[n-1]:
                newText.append('x')
        newText.append(i)
        n += 1
    if (len(newText) % 2 != 0):
        newText.append('x')
    return newText

        
def bagiDuaPlaintext(text):
    perDua = []
    group = 0
    for i in range(2, len(text), 2):
        perDua.append(text[group:i])
        group = i
    perDua.append(text[group:])
    return perDua

def searchKey(key, text):
    for i in range (5):
        for j in range (5):
            if text == key[i][j]:
                return i, j

def barisSama(key, baris, kolomA, kolomB):
    if kolomA == 4:
        enA = key[baris][0]
    else:
        enA = key[baris][kolomA+1]

    if kolomB == 4:
        enB = key[baris][0]
    else:
        enB = key[baris][kolomB+1]
    
    return enA, enB

def kolomSama(key, barisA, barisB, kolom):
    if barisA == 4:
        enA = key[0][kolom]
    else:
        enA = key[barisA+1][kolom]

    if barisB == 4:
        enB = key[0][kolom]
    else:
        enB = key[barisB+1][kolom]
    
    return enA, enB

def barisKolomBeda(key, barisA, barisB, kolomA, kolomB):
    enA = key[barisA][kolomB]
    enB = key[barisB][kolomA]

    return enA, enB


def encryptPlayfair(key, plaintext):
    encrypted = []
    key = key.replace(" ", "")
    key = key.lower()
    keyTable = createKeyTable(key)
    plaintext = plaintext.replace(" ", "")
    plaintext = plaintext.lower()

    text = bagiDuaPlaintext(ubahPlaintext(plaintext))

    for i in range(len(text)):
        barisA, kolomA = searchKey(keyTable, text[i][0])
        barisB, kolomB = searchKey(keyTable, text[i][1])

        if barisA == barisB:
            a, b = barisSama(keyTable, barisA, kolomA, kolomB)
        elif kolomA == kolomB:
            a, b = kolomSama(keyTable, barisA, barisB, kolomA)
        else:
            a, b = barisKolomBeda(keyTable, barisA, barisB, kolomA, kolomB)

        en = a + b
        encrypted.append(en)
    
    return encrypted

def deBarisSama(key, baris, kolomA, kolomB):
    if kolomA == 0:
        enA = key[baris][4]
    else:
        enA = key[baris][kolomA-1]

    if kolomB == 0:
        enB = key[baris][4]
    else:
        enB = key[baris][kolomB-1]
    
    return enA, enB

def deKolomSama(key, barisA, barisB, kolom):
    if barisA == 0:
        enA = key[4][kolom]
    else:
        enA = key[barisA-1][kolom]

    if barisB == 0:
        enB = key[4][kolom]
    else:
        enB = key[barisB-1][kolom]
    
    return enA, enB

def deBarisKolomBeda(key, barisA, barisB, kolomA, kolomB):
    enA = key[barisA][kolomB]
    enB = key[barisB][kolomA]

    return enA, enB

def decryptPlayfair(key, plaintext):
    decrypted = []
    key = key.replace(" ", "")
    key = key.lower()
    keyTable = createKeyTable(key)
    plaintext = plaintext.replace(" ", "")
    plaintext = plaintext.lower()
    
    text = bagiDuaPlaintext(plaintext)

    for i in range(len(text)):
        barisA, kolomA = searchKey(keyTable, text[i][0])
        barisB, kolomB = searchKey(keyTable, text[i][1])

        if barisA == barisB:
            a, b = deBarisSama(keyTable, barisA, kolomA, kolomB)
        elif kolomA == kolomB:
            a, b = deKolomSama(keyTable, barisA, barisB, kolomA)
        else:
            a, b = deBarisKolomBeda(keyTable, barisA, barisB, kolomA, kolomB)

        en = a + b
        decrypted.append(en)
    
    return decrypted