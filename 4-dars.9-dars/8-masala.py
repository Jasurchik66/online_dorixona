class Futbol_jamoasi:

    def __init__(self, nom, mamlakat):
        self.nom = nom
        self.mamlakat = mamlakat  
        self.oyinchilar = []

    def oyinchi_qosh(self, ism): 
        self.oyinchilar.append(ism)
        
    def oyinchilarni_chop_et(self):
        print(f"""
O'yinchilar tarkibi: {self.nom}
Mamlakat: {self.mamlakat}
O'yinchilar: {(self.oyinchilar)}
""") 
        
futbol = Futbol_jamoasi("Real Madrid jamoasi", "Ispaniya")

futbol.oyinchi_qosh("Karim Benzema")
futbol.oyinchi_qosh("Luka Modric")
futbol.oyinchi_qosh("Vinicius Jr")

futbol.oyinchilarni_chop_et()
