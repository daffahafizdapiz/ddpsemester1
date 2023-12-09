#Latihan_13_use_modul

print('---- Gunakan Modul ----')
import modul1
modul1.penjumlahan(5,2)
modul1.pengurangan(10,3)
modul1.perkalian(5,6)
modul1.operasi_gabungan(5,8,9)

print('---- Gunakan Modul dengan Alias ----')
import modul1 as hitung
hitung.pembagian(20,2)
hitung.perpangkatan(2,3)
hitung.pembagian_bulat(80,45)

print('---- Gunakan Modul dengan Sebagian fungsinya ----')
from modul1 import penjumlahan, pengurangan
penjumlahan(20,30)
pengurangan(6,3)

print('---- Gunakan Modul dengan memanggil semua fungsinya ----')
from modul1 import *
penjumlahan(20,30)
pengurangan(5,3)
perkalian(30,5)
pembagian(12,6)
pembagian_bulat(20,2)
perpangkatan(3,3)
hasil_bagi(35,5)
operasi_gabungan(8,20,9)
operasi_gabungan_lanjutan(25,3,15)
operasi_perkalian_lanjutan(5,6,10)

print('---- Gunakan Modul dengan memanggil sebagian fungsinya dengan Alias ----')
from modul1 import penjumlahan as add, perkalian as x, pengurangan as m
add(5,7)
x(6,10)
m(10,7)