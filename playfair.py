
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

