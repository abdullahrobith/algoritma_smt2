print(10*'=','aplikasi beasiswa',10*'=')
nama = str(input('Nama Mahasiswa : '))
umur = int(input('Umur : '))
pekerjaan_orang_tua = str(input('Pekerjaan Orang Tua : ').upper())
gaji_orang_tua = int(input('Gaji Orang Tua : '))
ipk = float(input('IPK Mahasiswa : '))

pekerjaan = ['POLRI','TNI','PNS']
if (pekerjaan_orang_tua not in pekerjaan) and (gaji_orang_tua <= 1000000) and (ipk >= 2.7) and (umur <= 25):
    print('Memenuhi Syarat Beasiswa👍')
else:
    print('Tidak Memenuhi Syarat Beasiswa, Tetap semangat dan jangan putus asa😘🙌')