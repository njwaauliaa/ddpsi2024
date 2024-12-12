from Animal import Animal

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, Bernapas, warna):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.bernapas = Bernapas
        self.warna = warna
        
    def cetak_ikan(self):
        super().cetak()
        print("Bernapas \t\t: ", self.bernapas, 
        "\nwarna \t\t\t: ", self.warna)
        
lele = Ikan("Lele", "Pelet", "Air tawar", "Bertelur", "Insan", "Hitam")
lele.cetak_ikan()
print("===========================================")
hiu =Ikan("Hiu", "Daging", "Laut", "Mamalia", "insang", "Abu-abu")
hiu.cetak_ikan()
