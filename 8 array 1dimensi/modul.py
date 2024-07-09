nilai_siswa = []
def inp():
    jumlah = int(input('Masukkan Jumlah Siswa : '))
    print(25*'=')
    for siswa in range(jumlah):
        nilai = float(input(f'Masukkan Nilai Siswa Ke-{siswa+1} : '))
        nilai_siswa.append(nilai)
    print(25*'=')

    jumlah_data = len(nilai_siswa)
    total_data = sum(nilai_siswa)
    rata_rata = total_data / jumlah_data
    print(f'Nilai Rata-rata Kelas : {rata_rata}')

    nilai_tertinggi = max(nilai_siswa)
    print(f'Nilai Tertinggi : {nilai_tertinggi}')

    nilai_terendah = min(nilai_siswa)
    print(f'Nilai Terendah : {nilai_terendah}')

    diatas_rata_rata = sum(True for i in nilai_siswa if i > rata_rata)
    print(f'Jumlah Siswa Diatas Rata-rata : {diatas_rata_rata}')

    nilai_siswa.sort()
    print(f'Urutan Nilai Dari Yang Terendah Ke Tertinggi : {nilai_siswa}')
    
    if len(nilai_siswa) >= 3:
        nilai_siswa.reverse()
        teratas = nilai_siswa[2]
        print(f'Nilai Tertinggi Ke tiga : {teratas}')
    else:
        print('Tidak ada cukup siswa untuk menentukan nilai tertinggi ketiga')
    print(30 * '=')