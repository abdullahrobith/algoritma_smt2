nilai = int(input('Masukkan Nilai [Range : 1-100] : '))
if nilai<0 or nilai>100:
     print('Error : Nilai Range 0-100')
     exit()

print('Benar')

if nilai > 80:
    print('Index A')
elif nilai > 65 and nilai < 80:
    print('Index B')
elif nilai > 50 and nilai < 65:
    print('Index C')
else:
    print('Index D')


#KONDISI BERSARANG
umur = int(input('Masukkan Umur : '))
if umur > 17:
    undangan = input('Punya Undangan [Y/T] : ').upper()
    if undangan == 'Y':
        print('Boleh Mencoblos')
    else:
        print('Daftar Pemilu')
else:
    print('Umur tidak memenuhi')