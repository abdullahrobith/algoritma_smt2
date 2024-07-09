i = 1
while i <= 10:
    print('Mari berhitung',i) #jika hanya seperti ini, maka output akan terus berjalan (Tidak berhenti), untuk menghentikan secara paksa klik ctrl + c pada terminal
    i += 1 #agar output bisa berhenti sesuai perintah i <= 10

print('\n')
#break = untuk menghentikan secara paksa
total_perulangan = 0
while True:
    main = input('Ingin keluar atau tidak ? [Y/T] : ').upper()
    if main == 'Y':
        break
    total_perulangan += 1
print('Total perulangan : ',total_perulangan)

print('\n')
while True:
    angka = int(input('Masukkan Angka : '))
    if angka % 2 == 0:
        print(angka,'Adalah angka genap')
    else:
        print(angka,'Adalah angka ganjil')