from Animal import Animal

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.racun = racun
        
    def cetak_ular(self):
        super().cetak()
        print("Design \t\t\t: ", self.design, 
        "\nRacun \t\t\t: ", self.racun)
        
anaconda = Ular("Anaconda", "Kambing", "Amazon", "Bertelur", "Batik solo", "Tidak berbisa")
anaconda.cetak_ular()
print("===========================================")
piton = Ular("Piton", "Monyet", "Hutan", "Bertelur", "Coklat", "Berbisa")
piton.cetak_ular()