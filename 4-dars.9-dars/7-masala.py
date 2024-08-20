class Kompaniya:

    def __init__(self, nom, soha):
        self.nom = nom
        self.soha = soha
        self.xodimlar = {}

    def xodim_qosh(self, ism, lavozim):
        self.xodimlar[ism] = lavozim

    def xodimlarni_chop_et(self):
        print(f"Kompaniya: {self.nom}\nSoha: {self.soha}\nXodimlar:")
        for ism, lavozim in self.xodimlar.items():
            print(f"- {ism}: {lavozim}")
    
kompaniya = Kompaniya("Toshkent", "Dasturlash")

kompaniya.xodim_qosh("Jasur", "Dasturchi")
kompaniya.xodim_qosh("Ali", "Boshqaruvchi")
kompaniya.xodim_qosh("Hasanboy", "Texnik")

kompaniya.xodimlarni_chop_et()
