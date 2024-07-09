from collections import deque

#Deklarasi Queue
antrian = deque()

def enqueue(item):
    antrian.append(item) #appendleft : data masuk dari sebelah kiri, sehingga data pertama menjadi urutan terakhir

def dequeue():
    antrian.popleft()

enqueue('adi')
enqueue('iqbal')
enqueue('supri')

dequeue()

print(antrian)