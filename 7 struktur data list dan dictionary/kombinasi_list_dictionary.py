person = [
    {'nama' : 'Dalim', 'umur' : 23},
    {'nama' : 'Izat', 'umur' : 25},
    {'nama' : 'Bagas', 'umur' : 20}
]

person_new = {'nama' : 'Wildan', 'umur' : 18}
person.append(person_new)

print(person)

for i in person:
    print('-',i['nama'],i['umur'])