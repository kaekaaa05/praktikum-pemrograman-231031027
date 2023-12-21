pswrd_benar = 'cinta ith'
maks_kesalahan = 3
kesalahan = 0

# Perulangan untuk maksimal tiga kali kesalahan
while kesalahan < maks_kesalahan:
    # Meminta pengguna memasukkan password
    password_input = input('Masukkan password: ')

    # Memeriksa apakah password yang dimasukkan benar
    if password_input == pswrd_benar:
        print('Selamat Anda login!')
        break  # Keluar dari perulangan jika password benar
    else:
        kesalahan += 1
        sisa_kesalahan = maks_kesalahan - kesalahan
        print(f'Password salah! Kesempatan anda tersisa {sisa_kesalahan} kali')

# Pesan jika kesalahan maksimal tercapai
if kesalahan == maks_kesalahan:
    print("Anda kehabisan kesempatan")

