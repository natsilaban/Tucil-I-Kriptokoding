import playfair as pf

print("Welcome to Tugas Kripto")

print("Apa cipher yang mau digunakan?\n [1] Vignere\n [2] Extended\n [3] Playfair\n")

cipher = int(input("Pilihanku: "))

print("Apakah yang ingin kamu lakukan?\n [1] enkripsi\n [2] dekripsi \n")

choice = int(input("Pilihanku: "))

key = input("Silakan masukkan key: ")

if choice == 1:
    plaintext = input("Silakan masukkan teks yang ingin dienkripsi: ")
else:
    plaintext = input("Silakan masukkan teks yang ingin didekripsi: ")

if cipher == 3:
    if choice == 1:
        encrypted = (pf.encryptPlayfair(key, plaintext))
        print("Hasil enkripsi: " + "".join(encrypted))
    else:
        decrypted = (pf.decryptPlayfair(key, plaintext))
        print("Hasil enkripsi: "+"".join(decrypted))