print("""
======================================
Sistem penghitung luas bangun datar)

Pilih bangun datar:
1 = Persegi
2 = Lingkaran
3 = Segitiga
""")

BangunDatar = int(input("Masukan pilihan bangun datar: "))

match BangunDatar:
    case 1:
        sisi = int(input("Masukan sisi"))
        hasil = int(sisi * sisi)
        print("Luas persegi yang memiliki sisi", sisi, "adalah", hasil)

    case 2:
        jarijari = int(input("Masukan jari-jari"))
        hasil = int (3.14 * jarijari * jarijari)
        print("Luas lingkaran yang memiliki jari-jari:", jarijari, "adalah", hasil)
        
    case 3:
        alas = int(input(("Masukan alas")))
        tinggi = int(input(("Masukan tinggi")))
        hasil = 0.5 * alas * tinggi
        print("Luas segitiga yang memiliki alas", alas, "dan tinggi", tinggi, "adalah", hasil)
    case _:
        print("Masukan Angka yang sesuai")