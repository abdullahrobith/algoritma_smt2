a = 10
b = 10
print('A > B = ', a>b) # Lebih dari
print(f'A > B = {a>b}') 
print(f'A == B = {a==b}') # Sama dengan
print(f'A != B = {a!=b}') # Tidak sama dengan
print(f'A >= B = {a>=b}') # Lebih dari sama dengan
print(f'A <= B = {a<=b}') # Kurang dari sama dengan

temperature = 25
if temperature >= 25:
    print('Suhu Panas')
else:
    print('Suhu Dingin')