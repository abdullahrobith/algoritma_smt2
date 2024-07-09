import random

# Memilih angka acak antara 1 dan 10
angka_acak = random.randint(1, 10)

# Inisialisasi jumlah tebakan
jumlah_tebakan = 0

while True:
    # Minta pemain untuk menebak
    tebakan = int(input("Tebak angka antara 1 dan 10: "))

    # Cek apakah tebakan terlalu tinggi
    if tebakan > angka_acak:
        print("Tebakan terlalu tinggi!")
    # Cek apakah tebakan terlalu rendah
    elif tebakan < angka_acak:
        print("Tebakan terlalu rendah!")
    # Jika tebakan benar
    else:
        print("Selamat! Tebakan Anda benar!")
        break

    # Increment jumlah tebakan
    jumlah_tebakan += 1

# Cetak jumlah tebakan yang diperlukan
print(f"Anda memerlukan {jumlah_tebakan} tebakan untuk menebak angka dengan benar.")