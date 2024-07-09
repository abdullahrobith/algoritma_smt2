buku = []
judul = str(input("Masukkan Judul : "))
tahun = int(input("Masukkan Tahun Terbit : "))
harga = float(input("Masukkan Harga : "))
penulis = str(input("Masukkan Penulis : "))
ketersediaan = bool(int(input("Masukkan Ketersediaan : ")))

data_buku = [judul,tahun,harga,penulis,ketersediaan]
buku.append(data_buku)
print(buku)