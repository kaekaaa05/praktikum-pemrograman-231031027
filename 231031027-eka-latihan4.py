print('##### LATIHAN 4 #####')

pendapatan = int(input('Pendapatan: '))

if pendapatan >= 5001 :
    presentase = 50

elif pendapatan > 4000 :
    presentase = 40

elif pendapatan > 3000 :
    presentase = 30

elif pendapatan > 2000 :
    presentase = 20

elif pendapatan > 1000 :
    presentase = 10

else :
     presentase = 0

bonus = pendapatan *(presentase / 100)
total = pendapatan + bonus

print('Pendapatan : ',pendapatan)
print('Presentase : ',presentase,"%")
print('Bonus : ',bonus)
print('Total Pendapatan : ',total)

