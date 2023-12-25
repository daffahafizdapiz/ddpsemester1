class Animal:
    def __init__(self, nama, makanan, habitat, reproduksi):
        self.nama = nama
        self.makanan = makanan
        self.habitat = habitat
        self.reproduksi = reproduksi

class Badak(Animal):
    def __init__(self, nama, makanan, habitat, reproduksi, panjang_tanduk, warna_kulit):
        super().__init__(nama, makanan, habitat, reproduksi)
        self.panjang_tanduk = panjang_tanduk
        self.warna_kulit = warna_kulit

    def info(self):
        print("------------------------------")
        print(f"Nama\t\t: {self.nama}\nMakanan\t\t: {self.makanan}\nHabitat\t\t: {self.habitat}\nReproduksi\t: {self.reproduksi}")
        print(f"Panjang Tanduk\t: {self.panjang_tanduk}\nWarna Kulit\t: {self.warna_kulit}")
        print("------------------------------")


class Ikan(Animal):
    def __init__(self, nama, makanan, habitat, reproduksi, panjang_sirip, warna):
        super().__init__(nama, makanan, habitat, reproduksi)
        self.panjang_sirip = panjang_sirip
        self.warna = warna


    def info(self):
        print(f"Nama\t\t: {self.nama}\nMakanan\t\t: {self.makanan}\nHabitat\t\t: {self.habitat}\nReproduksi\t: {self.reproduksi}")
        print(f"Panjang Sirip\t: {self.panjang_sirip}\nWarna\t\t: {self.warna}")
        print("------------------------------")


class Ular(Animal):
    def __init__(self, nama, makanan, habitat, reproduksi, panjang_tubuh, jenis_racun):
        super().__init__(nama, makanan, habitat, reproduksi)
        self.panjang_tubuh = panjang_tubuh
        self.jenis_racun = jenis_racun
        

    def info(self):
       print(f"Nama\t\t: {self.nama}\nMakanan\t\t: {self.makanan}\nHabitat\t\t: {self.habitat}\nReproduksi\t: {self.reproduksi}")
       print(f"Panjang Tubuh\t: {self.panjang_tubuh}\nJenis Racun\t: {self.jenis_racun}")
       print("------------------------------")


# Contoh penggunaan
badak = Badak("Badak Jawa", "Rumput", "Hutan", "Vivipar" , "30 cm", "Abu-abu")
badak.info()

ikan = Ikan("Ikan Koi", "Fish Food", "Akuarium", "Ovipar", "90 cm", "Putih/Merah")
ikan.info()

ular = Ular("Green Snack", "Rodents", "Hutan", "Ovipar", "7 m", "Neurotoksin")
ular.info()






