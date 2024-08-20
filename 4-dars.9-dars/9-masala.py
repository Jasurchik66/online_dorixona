class Universitet:
    def __init__(self, nom, manzil):
        self.nom = nom
        self.manzil = manzil
        self.talabalar = {} 

    def talaba_qosh(self, ism, kurs):
        self.talabalar[ism] = kurs

    def talabalarni_chop_et(self):
        talabalar_royxati = ([f"{ism}: {kurs}-kurs" for ism, kurs in self.talabalar.items()])
        print(f"""
Talabalar yo'nalishi: {self.nom}
Manzili: {self.manzil}
Talabalar:
{talabalar_royxati}
""")

univer = Universitet("TATU", "Toshkent")

univer.talaba_qosh("Akmal", 1)
univer.talaba_qosh("Jasur", 2)
univer.talaba_qosh("Aziz", 3)

univer.talabalarni_chop_et()
