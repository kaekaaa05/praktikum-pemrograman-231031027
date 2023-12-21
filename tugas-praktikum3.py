print('Tugas Praktikum 3'.center(40))
nama = 'Eka Tanduklangi\''
nim  = '231031027'
prodi= 'Sistem Informasi A'
print(f'''
Nama\t: {nama}
NIM\t: {nim}
prodi\t: {prodi}''')

'''Dari beberapa string berikut, buatkan manipulasi kode
agar hasil outpunya sesuai'''


print()
str1 = 'duFort Frankel Von Neumann'
up   = str1.upper()
print(up)
up = up.split()
print(up[-1],up[0],up[1],up[2])
#output: NEUMANN DUFORT FRANKEL VON

print()
str2 = 'duFort Frankel Von Neumann'
up   = str2.upper()
print(up)
up = up.split()
print(up[0][0],up[1][0],up[2][0],up[-1])
#output: DFV NEUMANN

print()
str3 = 'duFort Frankel Von Neumann'
up   = str3.upper()
print(up)
up = up.split()
print(up[0],up[1][0],up[2][0],up[-1][0])
#output: DUFORT FVN

print()
str4 = 'duFOrt Frankel Von Neumann'
a = str4.split()
print(a[-1][0],a[0],a[1][0],a[2][0])
#output: N duFort FV

print()
str5 = 'DuFort Frankel Von Neumann'
a = str5.upper()
b = a.strip('NEUMANN')
c = ('NEUMANN ')
d = b.lower()
print(c + d[0:1],d[2:3],d[15:16])
#output: NEUMANN d f v

print()
str6 = 'duFort Frankel Von Neumann'
str6 = str6.upper().split()
print(str6[3],str6[0][0] + str6[0][2] + str6[2][0])
#output: NEUMANN DFV

print()
str7 = '@duFort Frankel Von Neumann$'
a=str7.strip('@,$')
b = a.replace('Neumann','NEUMANN')
print(b)
#output: duFort Frankel Von NEUMANN

print()
str8 = '#duFort4Frankel4Von4Neumann$'
str8 = str8.strip('#$')
print(str8[0:6],str8[7:14],str8[15:18],str8[19:26])
#output: duFort Frankel Von Neumann

print()
str9 = '@duFort@-^Frankel*-(Von(-(Neumann$'
str9 = str9.replace('-', ' ')
str9 = str9.split()
print(str9[0].strip('@'),str9[1].strip('^*'),str9[2].strip('('),str9[3].strip('($'))
#output: duFort Frankel Von Neumann

print()
str10 = '@DUFort@1^FraNkel*1(VoN(1(NeuMann^'
str10 = str10.replace('1', ' ')
str10 = str10.split()
print(str10[0].strip('@').replace('DU','du'),str10[1].strip('^*').title(),str10[2].strip('(').title(),str10[3].strip('(^').title())
#output: duFort Frankel Von Neumann
