from queue import LifoQueue

#Deklarasi Stack
stack = LifoQueue() #Untuk menampung data. Apabila ingin dibuat static maka ditambahkan 'maxsize='

#Tambah Data Stack
stack.put('Abdul')
stack.put('Lasso')
stack.put('Husain')
stack.put('Iqbal')

#Display Stack
print(stack.queue)

#Menampilkan Top Elemen Stack
print(f'Top/Peek Stack : {stack.queue[-1]}')

#Menghapus Data Pada Elemen Terakhir
stack.get()

#Mengecek Stack Kosong Atau Tidak
print(f'Stack Kosong/Tidak : {stack.empty()}')

#Memeriksa Apakah Stack Penuh
print(f'Stack Full / Tidak : {stack.full()}') #Jika menggunakan stack dinamic maka akan selalu menampilkan False

#Menentukan Jumlah Stack
print(f'Jumlah Stack : {stack.qsize()}')