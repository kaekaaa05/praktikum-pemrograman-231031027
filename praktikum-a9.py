def judul():
    print('=== Praktikum 9 ===')
    print('PROGRAM MENGHITUNG LUAS DAN KELILING'.center(30))
    print('BANGUN DATAR PERSEGI'.center(35))
    print()

def inputan():
    panjang = float(input('Masukkan Panjang: '))
    lebar = float(input('Masukkan Lebar: '))
    return panjang,lebar

def hitung(panjang,lebar):
    luas = panjang*lebar
    kel = (panjang+lebar)*2
    return luas,kel

def tampil(pesan,nilai):
    print(f'Hasil Perhitungan nilai {pesan}: {nilai}')

def pilihan():
    pilih = input('Apakah Ingin Melanjutkan? [y/n]: ')
    if pilih == 'y':
        a = True
    else:
        a = False
        print('Sampai Jumpaaaaa.')
    return a



a = True
while a:
    # Judul
    judul()

    # inputan panjang dan lebar
    panjang,lebar = inputan()

    # hitung luas
    luas,kel = hitung(panjang,lebar)

    # cetak atau display
    tampil('luas',luas)
    tampil('keliling',kel)

    # pilihan
    a = pilihan()
