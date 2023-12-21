biodata = {'nama'           : 'Eka Tanduklangi\'',
            'nim'           : '231031027',
            'prodi'         : 'Sistem Informasi',
            'TTL'           : 'Tokesan, 25 Agustus 2005',
            'asal'          : 'Toraja',
            'alamat'        : 'Galung Maloang',
            'agama'         : 'Kristen',
            'hobi'          : 'Mendengarkan Musik',
            'nama orang tua': {'Ayah' : 'Marthen Sulle',
                                'Ibu' : 'Esther Doming',}
                            
}



print()
print(biodata)
print()
print('Nama :'(biodata['nama']))
print('Biodata :')
print(biodata['nama'])
print(biodata.get('nim'))
print(biodata.get('prodi'))
print(biodata.get('asal'))
print(biodata['agama'])
print(biodata['nama orang tua']['Ayah'])

