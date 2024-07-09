string1 = 'hello'
string2 = 'world!'
int1 = 10
print(string1 + " " + string2) #tanda petik2 berfungsi sebagai spasi
print((string1 + " ")*10)
print(string1 + str(int1)) #integer harus diubah menjadi string

daftar_kata = ['aku','seorang','kapiten']
kalimat =" ".join(daftar_kata) #untuk mengubah list menjadi kalimat (menggabungkan string)
print(kalimat)

daftar_kata1 = 'Aku seorang programmer, dia juga programmer'
pisah_kata = daftar_kata1.split() #untuk mengubah kalimat menjadi list(memisahkan string)
print(pisah_kata)

substring = daftar_kata1.replace('programmer','design') #untuk mengubah substring
print(substring)
print(daftar_kata1[0:11]) #untuk memanggil sebagian kalimat