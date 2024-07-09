person = {'nama' : 'Noah', 'umur' : 23, 'kota' : 'Kota Tegal'}

person['fav'] = 'Bakso' #untuk menambahkan key atau variabel baru
print(person)

person['umur'] = 17 #untuk mengubah/meng update data yang sudah ada dalam variabel
print(person)

del person['kota'] #untuk menghapus key dan value
print(person)

print(person['nama']) #untuk memanggil value dalam dictionary