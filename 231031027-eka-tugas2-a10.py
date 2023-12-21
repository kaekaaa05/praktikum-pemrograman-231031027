print(f'1. Program Penjumlahan Waktu\n')
# Input waktu awal dalam format jam dan menit
waktu_awal = input('Masukkan waktu awal (hh:mm): ')
jam_awal, menit_awal = map(int, waktu_awal.split(':'))

# Input jumlah jam dan menit yang akan ditambahkan
jam_tambahan = int(input('Masukkan jumlah jam yang akan ditambahkan: '))
menit_tambahan = int(input('Masukkan jumlah menit yang akan ditambahkan: '))

# Jumlahkan waktu
jam_total = jam_awal + jam_tambahan
menit_total = menit_awal + menit_tambahan

# Penanganan jika menit > 60
if menit_total >= 60:
    jam_total += 1
    menit_total -= 60
# Penanganan jika jam lebih dari 24 (untuk menghindari lebih satu hari)
if jam_total >= 24:
    jam_total -= 24

# Format hasil ke fotmat hh:mm
hasil = f'{jam_total:02d}:{menit_total:02d}'

print(f'Waktu sekarang menunjukkan pukul {hasil}')


print()
print(f'2. Program Selisih Waktu')
# Input waktu awal dalam format jam dan menit
waktu_awal = input('Masukkan waktu awal (HH:MM): ')
jam_awal, menit_awal = map(int, waktu_awal.split(':'))

# Input jumlah jam dan menit yang akan diselisih
kurang_jam = int(input('Kurang berapa jam: '))
kurang_menit = int(input('Kurang berapa menit: '))


# kurangi waktu
jam_akhir = jam_awal - kurang_jam
menit_akhir = menit_awal - kurang_menit

# Jika menit < 0, pinjam 60 menit dari jam sebelumnya
if menit_akhir < 0:
    jam_akhir -= 1
    menit_akhir += 60

# Jika menit < 0, pinjam 60 menit dari jam sebelumnya
if jam_akhir < 0:
    jam_akhir += 24

# Format hasil ke fotmat hh:mm
hasil = f'{jam_akhir:02d}:{menit_akhir:02d}'

print(f'Waktu sekarang menunjukkan pukul {hasil}')