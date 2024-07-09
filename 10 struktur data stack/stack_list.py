#Deklarasi Stack
stack = []

#Tambah Data Stack
stack.append('lord alul')
stack.append('iqbal')
stack.append('husain')
stack.append('mbape')

#Display Stack
for index,value in enumerate(stack):
    print(f'{index} : {value}')

#Hapus Data Pada Elemen Terakhir
stack.pop()
for index,value in enumerate(stack):
    print(f'{index} : {value}')

#Mengecek Data Elemen Top/Peek
print(f'Data Stack Top : {stack[-1]}')

#Mengecek Apakah stack isEmpty
print('Stack Kosong : ')
print('Ya' if len(stack) == 0 else 'Tidak')

#Mengecek Jumlah Elemen Stack
print(f'Jumlah Elemen Stack : ',len(stack))