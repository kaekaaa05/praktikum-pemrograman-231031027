print('praktikum-a4\n')

nim = ['2','3','1','0','3','1','0','2','7']
# nim2 = '231031027'
print(nim)
# print(nim2[1:3])

# akses item
print (f'item indeks 0: {nim[0]}')
print (f'item indeks 4: {nim[4]}')
print (f'item indeks terakhir: {nim[len(nim)-1]}')

# akses indeks negatif
print (f'item terakhir: {nim[-1]}')
print (f'item pertama: {nim[-len(nim)]}')
print (f'item indeks 6 [-3]: {nim[-3]}')
print (f'item indeks 4 [-5]: {nim[-5]}')
print (f'item indeks 7 [-2]: {nim[-2]}')

# akses inddeks batas
print (f'item indeks 1,2,....: \n {nim[1:]}')
print (f'item indeks 3,4,....: \n {nim[3:]}')
print (f'item indeks 0,1,2: \n {nim[:3]}')
print (f'item indeks 0,1,2,3: \n {nim[:4]}')
print (f'item indeks semua: \n {nim[:]}')

print (f'item indeks [:8]: \n {nim[:-1]}')
print (f'item indeks [:6]: \n {nim[:-3]}')

# pengirisan
print (f'item indeks 1,2 : \n {nim[1:3]}')
print (f'item indeks 2,3,4 : \n {nim[2:5]}')
print (f'item indeks kosong: \n {nim[3:3]}')
print (f'item indeks [8:8] kosong: \n {nim[-1:-1]}')
print (f'item indeks [1:8] : \n {nim[1:-1]}')
print (f'item indeks [2:7] : \n {nim[2:-2]}')

#       LATIHAN LIST

data = ['Eka Tanduklangi\'',2023,'Aktif']
nilai= [90,89,93,97]

print('Nama: '+ data[0])
print('angkatan:', data[1])
print('status: '+ data[2])

#  Eka Tandukangi' status Kuliah: Aktif
print(f'{data[0]} status kuliah {data[2]}')

#  Data terbesar nilai adalah: 97
print(f'Data terbesar nilai adalah: {max(nilai)}')

#  Data terkecil nilai adalah: 89
print(f'Data terkecil nilai adalah: {min(nilai)}')

# Rata-rata nilai adalah: 92.25
x_bar = sum(nilai)/len(nilai)
print(f'Rata-rata nilai adalah: {x_bar}')

#       LATIHAN TUPLE

data = ('Eka Tanduklangi\'',2023,'Aktif')
nilai= (90,89,93,97)

print(data[1])
print(data[-1])
print(nilai[1:-1])

# Jumlah nilai mahasiswa adalah: 4
print(f'Jumlah nilai mahasiswa adalah: {len(nilai)}')

# Data terbesar nilai adalah: 97
print(f'Data terbesar nilai adalah: {max(nilai)}')

# Data terkecil nilai adalah: 89
print(f'Data terkecil nilai adalah: {min(nilai)}')

# Rata-rata nilai adalah: 92.25
x_bar = sum(nilai)/len(nilai)
print(f'Rata-rata nilai adalah: {x_bar}')

print()
#       LATIHAN NESTED LIST
data=[['Eka Tanduklangi\'',2023,'aktif'],
      [90,89,93,97],
      [20,22],
      ['S1-Reguler','Ganjil']]

matkul = ['Agama Kristen','Pancasila','Bahasa Indonesia','CINTA']
sks    = [2,2,2,2]
# Tambahkan matkul dan sks ke dalam data (di akhir)
data.append(matkul)
data.append(sks)

# Mata kuliah 1: Matkul1 dengan jumlah 2 sks
print(f'Mata Kuliah 1: {data[4][0]} dengan jumlah {data[-1][0]} sks\n')
# Mata kuliah 2: Matkul2 dengan jumlah 2 sks
print(f'Mata Kuliah 2: {data[4][1]} dengan jumlah {data[-1][1]} sks\n')
# Mata kuliah 3: Matkul3 dengan jumlah 2 sks
print(f'Mata Kuliah 3: {data[4][2]} dengan jumlah {data[-1][2]} sks\n')
# Mata kuliah 4: Matkul4 dengan jumlah 2 sks
print(f'Mata Kuliah 4: {data[4][3]} dengan jumlah {data[-1][3]} sks\n')
data[4].append('Pengantar Pemrograman')
data[5].append(3)

# Tambahkan 3 matkul dengan sks nya
data[4].append('Pengantar Teknologi Informasi')
data[5].append(3)
data[4].append('Kalkulus Dasar 1')
data[5].append(3)
data[4].append('Sains Terpadu')
data[5].append(3)

# Mata kuliah 5: Matkul5 dengan jumlah .. sks
print(f'Mata Kuliah 5: {data[4][4]} dengan jumlah {data[-1][4]} sks\n')
# Mata kuliah 6: Matkul6 dengan jumlah .. sks
print(f'Mata Kuliah 6: {data[4][5]} dengan jumlah {data[-1][5]} sks\n')
# Mata kuliah 7: Matkul7 dengan jumlah .. sks
print(f'Mata Kuliah 7: {data[4][6]} dengan jumlah {data[-1][6]} sks\n')
# Mata kuliah 8: Matkul8 dengan jumlah .. sks
print(f'Mata Kuliah 8: {data[4][7]} dengan jumlah {data[-1][7]} sks\n')


# Tambahkan 8 nilai masing-masing

print(data[0][0])
print(data[3][0])
print(data[2][0:])

# >> Tugas: Nama Mahasiswa Eka Tanduklangi' dengan NIM: 231031027
print(f'Nama Mahasiswa {data[0][0]} dengan NIM {"".join(nim)}')

# Program pendidikan Eka Tanduklangi': S1-Reguler
print(f'Program pendidikan {data[0][0]}: {data[3][0]}')

# Angkatan : 2023-Ganjil
print(f'Angkatan : {data[0][1]}-{data[3][1]}')

# Jumlah nilai Eka Tanduklangi' adalah: 4
print(f'Jumlah nilai {data[0][0]} adalah: {len(data[1])}')

# Data terbesar Eka Tanduklangi' adalah: 97
print(f'Data terbesar nilai {data[0][0]} adalah: {max(data[1])}')

# Data terkecil Eka Tanduklangi' adalah: 89
print(f'Data terkecil {data[0][0]} adalah: {min(data[1])}')

# Rata-rata nilai Eka Tanduklangi' adalah: 92.25
x_bar = sum(data[1])/len(data[1])
print(f'Rata-rata nilai {data[0][0]} adalah: {x_bar}')


































