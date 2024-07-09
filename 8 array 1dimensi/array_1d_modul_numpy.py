import numpy as np

array_1d = np.array([90,70,40,30,20,10])
print(array_1d)

rata_rata = np.mean(array_1d)
print(np.mean(array_1d)) #Menampilkan Rata-rata
print(np.median(array_1d)) #Menampilkan Nilai Tengah
print(np.max(array_1d)) #Menampilkan Nilai Tertinggi
print(np.min(array_1d)) #Menampilkan Nilai Terendah
print(np.sum(array_1d > rata_rata)) #Menampilkan Jumlah Nilai Yang Ada Diatas Rata-rata
print(array_1d[array_1d > rata_rata]) #Menampilkan Nilai Yang Ada Diatas Rata-rata