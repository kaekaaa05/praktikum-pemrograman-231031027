psw = [1020,
       4030,
       8880]

max_ksmptn = 3

while True:
    if max_ksmptn  != 0:
        try:
            inp = int(input('Masukkan password 1: '))
            if inp == psw[0]:
                print('Password Benar!')
                inp = int(input('Masukkan password 2: '))
                if inp ==psw[1]:
                    print('Password Benar!')
                    inp = int(input('Masukkan password 3: '))
                    if inp == psw[2]:
                        print('Selamat Anda login!')
                        break
                    elif inp != psw[2]:
                        max_ksmptn  -= 1
                        print(f"Password salah! Anda memiliki {max_ksmptn} kesempatan lagi.")
                        continue
                    else:
                        print("Akun terkunci! Silahkan coba lain kali.")
                        break
                elif inp != psw[1]:
                    max_ksmptn  -= 1
                    print(f"Password salah! Anda memiliki {max_ksmptn} kesempatan lagi.")
                    continue
                else:
                    print("Akun terkunci! Silahkan coba lain kali.")
                    break
            elif inp != psw[0]:
                max_ksmptn -= 1
                print(f"Password salah! Anda memiliki {max_ksmptn} kesempatan lagi.")
                continue
        except ValueError:
            print('Mohon masukkan format dengan benar!')
            max_ksmptn  -= 1
            print(f'Anda memiliki {max_ksmptn} kesempatan tersisa!')
    else:
        print('Anda terblokir. kesempatan anda telah habis.')
        break


