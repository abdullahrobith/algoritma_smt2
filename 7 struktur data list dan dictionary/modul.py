def tampilan():
    print ('selamat datang di program manajemen stok barang')
    print('='*25)
    print ('1. Tambah Data Barang')
    print ('2. Hapus Data Barang')
    print ('3. Tampilkan Data Barang')
    print ('4. Keluar')
    print('='*25)

barang = []

def insert():
    nama = str(input('Masukan Nama Barang : '))
    stok = str(input('Masukan Stok Barang : '))
    data_baru = {'nama barang':nama,'stok':stok}
    barang.append(data_baru)

def delete():
    hapus = int(input('Hapus Data Index Ke : '))
    del barang[hapus]

def total():
    print('data barang elektronik'.upper())
    for a in barang:
        print(a['nama barang'],':',a['stok'])