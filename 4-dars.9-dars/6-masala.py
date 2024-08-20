class Musobaqa:

    def __init__(self, nom, joy):
        self.nom = nom
        self.joy = joy
        self.ishtirokchilar = []

    def ishtirokchi_qosh(self, ism):
        self.ishtirokchilar.append(ism)
        print(f"{ism} ishtirokchi  qo'shildi.")

    def ishtirokchilarni_chop_et(self):
        print(f"{self.nom} musobaqasidagi ishtirokchilar:")
        for ism in self.ishtirokchilar:
            print(f"- {ism}")

musobaqa = Musobaqa("Yugurish musobaqasi", "Toshkent")

musobaqa.ishtirokchi_qosh(["Jasur","Asror","Ali"])


musobaqa.ishtirokchilarni_chop_et()
