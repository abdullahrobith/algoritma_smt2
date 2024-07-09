# Deklarasi Array 1 Dimensi
nilai_siswa = [90,60,30,40,60]

# Akses Nilai Array
print(nilai_siswa[3])

# Menambah Data Pada Urutan Terakhir
nilai_siswa.append(100)
print(nilai_siswa)

# Menghapus Data Sesuai Indeks
nilai_siswa.pop(4) # Jika didalam () kosong, maka yang terhapus adalah nilai yang terakhir
print(nilai_siswa)

jumlah_data = len(nilai_siswa) # Menampilkan jumlah / panjang data
total_data = sum(nilai_siswa) # Menampilkan total Keseluruhan Dari Data
rata_rata = total_data / jumlah_data 
nilai_tertinggi = max(nilai_siswa)
nilai_terendah = min(nilai_siswa)

jumlah_nilai_diatas_rata_rata = sum(True for i in nilai_siswa if i > rata_rata) # Menampilkan Jumlah Nilai Yang Diatas Rata-rata
nilai_diatas_rata_rata = [i for i in nilai_siswa if i > rata_rata] # Menampilkan Nilai Yang Diatas Rata-rata

nilai_siswa.sort() # Mengurutkan Dari Yang Terkecil ke Terbesar
nilai_siswa.reverse() # Untuk Membalikkan Nilai, Dari yang terakhir menjadi terdepan (Bukan Mengurutkan Dari Terbesar Ke Terkecil)

print(f'Jumlah Data : {jumlah_data}')
print(f'Total Data : {total_data}')
print(f'Rata-rata Nilai : {rata_rata}')
print(f'Nilai Tertinggi : {nilai_tertinggi}')
print(f'Nilai Terendah : {nilai_terendah}')
print(f'Jumlah Nilai Diatas Rata-rata : {jumlah_nilai_diatas_rata_rata}')
print(f'Nilai Diatas Rata-rata : {nilai_diatas_rata_rata}')
print(f'Data Urut : {nilai_siswa}')