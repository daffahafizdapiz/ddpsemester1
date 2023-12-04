def duplikasi(list_buah):
    list_duplikasi = []
    for buah in list_buah:
        list_duplikasi.extend([buah, buah])
    return list_duplikasi

# Contoh
list_buah_asli = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
list_hasil_duplikasi = duplikasi(list_buah_asli)
print(list_hasil_duplikasi)
