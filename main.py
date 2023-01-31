print("Welcome to Tugas Kripto")

print("Apakah yang ingin kamu lakukan?\n [1] enkripsi\n [2] dekripsi \n")

choice = int(input("Pilihanku: "))

key = input("Silakan masukkan key: ")

if (choice == 1):
    plaintext = input("Silakan masukkan teks yang ingin dienkripsi: ")
else:
    encrypted = input("Silakan masukkan teks yang ingin didekripsi: ")
