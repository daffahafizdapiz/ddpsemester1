def balikan_list(list_buah):
    list_terbalik = []
    for i in range(len(list_buah)):
        list_terbalik.insert(0, list_buah[i])
    return list_terbalik

# Contoh 
list_asli = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
list_hasil_terbalik = balikan_list(list_asli)
print(list_hasil_terbalik)
