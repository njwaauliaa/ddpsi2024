from Animal import Animal

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, bunyi, warna):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.bunyi = bunyi
        self.warna = warna
        
    def cetak_burung(self):
        super().cetak()
        print("Bunyi \t\t\t: ", self.bunyi, 
        "\nWarna \t\t\t: ", self.warna)
        
lovebird = Burung("Lovebird", "Biji-bijian", "Pohon", "Bertelur", "Cicicuit", "Biru")
lovebird.cetak_burung()
print("===========================================")
merpati = Burung("Merpati", "Buah dan Sayuran", "Pesisir Pantai", "Bertelur", "akhakh", "Putih")
merpati.cetak_burung()