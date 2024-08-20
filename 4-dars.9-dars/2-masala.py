class Avtomobil:

    def __init__(self,model,yil,tezlik):
        self.model = model
        self.yil = yil
        self.tezlik = tezlik
  
    def tezlikni_oshir(self,qadam):
        self.tezlik += qadam
    
    def malumotni_chop_et(self):
        print(f"{self.model}  mashinasinig  yili {self.yil}  tezligi  {self.tezlik}")

avtomobil = Avtomobil("Supra",2024,420)

avtomobil.tezlikni_oshir(20)


avtomobil.malumotni_chop_et()
    
