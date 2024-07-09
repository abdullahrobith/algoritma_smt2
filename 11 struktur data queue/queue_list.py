# Deklarasi queue
queue = []

#Fungsi Tambah Data Queue
def enqueue(item):
    queue.append(item)

#Fungsi Hapus Data Queue
def dequeue():
    if len(queue) < 1:
        print('Data Kosong : Tidak Bisa Dihapus')
    else:
        queue.pop(0)

#Fungsi Mengakses Elemen Pertama
def front():
    if len(queue) < 1:
        return 'Queue Kosong'
    else:
        return queue[0]
    
#Fungsi Mengakses Elemen Terakhir
def tail():
    if len(queue) < 1:
        return 'Queue Kosong'
    else:
        return queue[-1]

#Fungsi Mengecek Queue Kosong Tidak
def isEmpty():
    if len(queue) == 0:
        return 'Queue Kosong'
    else:
        return 'Queue Tidak Kosong'

#Panggil Fungsi Enqueue
enqueue('Nugi')
enqueue('Saiful')
enqueue('Fulan')

#Panggil Fungsi Dequeue
dequeue()

print(queue)
print(f'Data Front : {front()}')
print(f'Data Tail : {tail()}')
print(f'Apakah Queue Kosong : {isEmpty()}')