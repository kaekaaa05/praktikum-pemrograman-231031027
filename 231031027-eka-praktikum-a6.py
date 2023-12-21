a = True

# Perulangan while dengan kondisi a
while a:
    # Input perulangan
    pilih = input('Pilihan: ')
    # Evaluasi pilihan
    if pilih == 'ya':
        print('Selamat Datang')
        # Mengubah nilai a menjadi false untuk menghentikan perulangan
        a = False
    elif pilih == 'tidak':
        print('Sampai Jumpa')
        # Mengubah nilai a menjadi false untuk menghentikan perulangan
        a = False
    else:
        print('Orang asing dilarang masuk')
        # Menggunakan True untuk tetap melanjutkan perulangan
        a = True