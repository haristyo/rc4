from Crypto.Cipher import ARC4

# Baca teks dari file plaintext.txt
with open('plaintext.txt', 'r') as file:
    plaintext = file.read()

# Kunci RC4 (disarankan untuk mengganti kunci ini)
key = b'KunciRahasia'

# Inisialisasi objek RC4
cipher = ARC4.new(key)

# Enkripsi teks
ciphertext = cipher.encrypt(plaintext.encode())

# Simpan hasil enkripsi ke dalam file RC4_encrypted.txt
with open('RC4_encrypted.txt', 'wb') as file:
    file.write(ciphertext)

print("Pesan telah dienkripsi dan disimpan dalam RC4_encrypted.txt")

with open('RC4_encrypted.txt', 'rb') as file:
    encryptedFile = file.read()


# Inisialisasi objek RC4
cipherDecrypt = ARC4.new(key)

# Dekripsi teks
ciphertextDecrypt = cipherDecrypt.decrypt(encryptedFile)

# Simpan hasil dekripsi ke dalam file RC4_decripted.txt
with open('RC4_decripted.txt', 'w') as file:
    file.write(ciphertextDecrypt.decode())

print("Pesan telah didekripsi dan disimpan dalam RC4_decripted.txt")