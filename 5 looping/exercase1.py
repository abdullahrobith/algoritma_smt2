jumlah_siswa = int(input('Masukkan Jumlah Siswa : '))
print(20*'=')
total_nilai = 0
for siswa in range(jumlah_siswa):
    nilai = float(input(f"Masukkan Nilai Siswa {siswa + 1} : "))
    total_nilai += nilai
rata_rata = total_nilai / jumlah_siswa
print(20*'=')
print("Rata rata nilai dari",jumlah_siswa,"siswa adalah : ",rata_rata)
