import playfair as pf
import vigenere_alphabet as va
import onetimepad as otp
import vigenere_extended as ve

print("Apa cipher yang mau digunakan?\n [1] Vignere\n [2] Extended Vigenere \n [3] Playfair\n [4] One-Time Pad")

cipher = int(input("Pilihanku: "))

print("Apakah yang ingin kamu lakukan?\n [1] enkripsi\n [2] dekripsi \n")

choice = int(input("Pilihanku: "))

if choice == 1:
    plaintext = input("Silakan masukkan teks yang ingin dienkripsi: ")
else:
    plaintext = input("Silakan masukkan teks yang ingin didekripsi: ")

if cipher == 1:
    key = input("Silakan masukkan key: ")
    if choice == 1:
        encrypted = va.encryptText(plaintext, key)
        print("Hasil enkripsi: " +encrypted)
    else:
        decrypted = va.decryptText(plaintext, key)
        print("Hasil dekripsi: "+decrypted)

elif cipher == 2:
    key = input("Silahkan masukkan key: ")
    if choice == 1:
        encrypted = ve.encryptExt(plaintext, key)
        print("Hasil enkripsi: "+ encrypted)
    else:
        decrypted = ve.decryptExt(plaintext, key)
        print("Hasil dekrpsiL "+ decrypted)

elif cipher == 3:
    key = input("Silakan masukkan key: ")
    if choice == 1:
        encrypted = (pf.encryptPlayfair(key, plaintext))
        print("Hasil enkripsi: " + "".join(encrypted).upper())
    else:
        decrypted = (pf.decryptPlayfair(key, plaintext))
        print("Hasil dekripsi: "+"".join(decrypted).upper())

elif cipher == 4:
    filename = input("Input filename (without extension): ")

    if choice == 1:
        filetext = filename + '.txt'
        otp.generateRandomKey(filetext)
        
        key = otp.getKey(filetext, plaintext)
        encrypted = (va.encryptText(plaintext, key))
        print("Hasil enkripsi: " + "".join(encrypted))
    else:
        filetext = filename + '.txt'
        key = otp.getKey(filetext, plaintext)
        decrypted = (va.decryptText(plaintext, key))
        print("Hasil dekripsi: "+"".join(decrypted))
