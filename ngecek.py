# plaintext = input("euy naon: ")
# key = input("keynya janlup: ")

# letters = []
# for i in key:
#     if i not in letters:
#         if i != 'j':
#             letters.append(i)

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
#         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# for i in alphabet:
#     if i not in letters:
#         letters.append(i)

# matrix = []
# while letters != []:
#     matrix.append(letters[:5])
#     letters = letters[5:]

# print(matrix)



# newText = []
# n = 0
# for i in plaintext:
#     if i == 'j':
#         i = 'i'
#     if (n != 0):
#         if (plaintext[n] == plaintext[n-1]):
#             newText.append('x')
#     newText.append(i)
    
    
#     n += 1
# if (len(newText) % 2 != 0):
#     newText.append('x')

# print(newText)

# perDua = []
# group = 0
# for i in range(2, len(newText), 2):
#     perDua.append(newText[group:i])
#     group = i
# perDua.append(newText[group:])

# print(perDua)

# # def search(mat, element):
# #     for i in range(5):
# #         for j in range(5):
# #             if(mat[i][j] == element):
# #                 return i, j

# # print(search(matrix, perDua[0][0]))

print(ord('A'))