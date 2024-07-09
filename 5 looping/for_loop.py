for i in range(5):
    print('Ayo Berhitung', i)

#pengulangan data list
fruits = ['apel', 'duren', 'pisang', 'melon']
numbers = [1,3,5,7,9]

print('\n') 
for buah in fruits: #variabel setelah kata 'for' = bebas
    print(buah)

print('\n')
for index,buah in enumerate(fruits): #untuk mengambil nilai indeks dari data list
    print(index,buah)

print('\n')
for nomor,buah in zip(numbers,fruits): #untuk menggabungkan 2 data list
    print(nomor,buah)

print('\n')
#pengulangan data String
names = "Abdullah Robithul Hasan"
for nama in names:
    print(nama)

print('\n')
#pengulangan data dictionary
biodata = {'Nama':'Abdullah','NIM':23090116}

for data in biodata:
    print(data) #jika seperti ini maka output hanya akan menampilkan labelnya saja

print('\n')
for value in biodata.values():
    print(value) #output akan menampilkan nilai/value nya saja

print('\n')
for label,value in biodata.items():
    print(label,':',value) #output akan menampilkan label dan nilainya

print('\n')
for i in range(1,11):
    if i % 2 == 0:
        print(i,'adalah bilangan genap')
    else:
        print(i,'adalah bilangan ganjil')
