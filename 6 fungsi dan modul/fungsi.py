#fungsi tanpa parameter
def cetak_string():
    print('Ini fungsi string')
cetak_string() #untuk memanggil output

#fungsi dengan parameter
def sapaan(ucapan):
    print(ucapan)
sapaan('ini fungsi')


def penjumlahan(a,b):
    hasil = a + b
    print(hasil)
penjumlahan(5,10)


def pengurangan(a,b):
    return a - b
print(pengurangan(10,5))


def bilangan(angka):
    if angka % 2 == 0:
        return 'Genap'
    else:
        return 'Ganjil'
print(bilangan(7))