a = 10
b = 10
print('nilai a',a,'id =',hex(id(a)))
print('nilai b',b,'id =',hex(id(b)))
print(a is b) # True karena nilainya sama (dianggap 1 objek)/ karena id nya sama
# khusus type data int, string, dan tuple

list1 = [1,2,3]
list2 = [1,2,3]
print(list1 is list2) # False karena type data list dan dictionary bersifat independen
# type data list dan dictionary mempunyai memori tersendiri (objeknya berbeda walaupun nilai nya sama)
# memori = variabel yang menyimpan nilai

list3 = [1,2,3]
list4 = list3
list3.append(6)
print(list3,list4)
print(list3 is list4) # True karena dianggap 1 objek