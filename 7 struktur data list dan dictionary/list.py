person = ['Dimas','Bagas','Idris','Izat']

person.append('Wildan') #untuk menambahkan data di akhir elemen
print(person)

person.insert(1,'Dulah') #untuk menambahkan data berdasarkan indeks
print(person)

person.remove('Dimas') #menghapus berdasarkan value nya
print(person)

del person[4] #untuk menghapus data berdasarkan indeks
print(person)

person.pop(3) #untuk menghapus data berdasarkan indeks, namun jika () kosong maka yang terhapus adalah data yang terakhir
print(person)