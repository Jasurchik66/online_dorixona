class Kutubxona:

    def __init__(self,nom,kitoblar):
        self.nom = nom
        self.kitoblar = kitoblar
       
    def kitob_qosh(self,nom):
        self.kitoblar.append(nom)


    def kitoblarni_chop_et(self):
        print(f" Kitoblar ro'yhati {self.kitoblar}")

kitob = Kutubxona("Adabiy",["Alpomish","Molxona"])

kitob.kitob_qosh("Hamsa")
kitob.kitob_qosh("Sariq Devni Minib")
kitob.kitob_qosh("Yovuz Daxo")



kitob.kitoblarni_chop_et()

