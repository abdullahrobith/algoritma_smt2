nama = str(input('Nama Karyawan : '))
jam_kerja = int(input('Jam Kerja Dalam 1 Hari : '))
tarif = int(input('Tarif per jam : '))

jam_kerja *= 20
gaji_sebulan = jam_kerja * tarif

print(nama, 'memiliki gaji', gaji_sebulan, 'selama 1 bulan')