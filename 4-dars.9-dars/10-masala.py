class Restoran:
    def __init__(self, nom, manzil):
        self.nom = nom
        self.manzil = manzil
        self.menu = {} 

    def taom_qosh(self, taom, narx):
        self.menu[taom] = narx

    def menuni_chop_et(self):
        print(f"\nRestoran: {self.nom} | Manzil: {self.manzil}")
        print("Menu:")
        for taom, narx in self.menu.items():
            print(f"{taom}: {narx} so'm")

restoran = Restoran("Osh Markazi", "Toshkent, Chilonzor")

restoran.taom_qosh("Osh", 20000)
restoran.taom_qosh("Manti", 15000)
restoran.taom_qosh("Somsa", 8000)

restoran.menuni_chop_et()
