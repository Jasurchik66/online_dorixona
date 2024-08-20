class Menejer:
    def __init__(self, ism, bolim):
        self.ism = ism
        self.bolim = bolim
        self.xodimlar = []

    def xodim_qosh(self, ism):
        self.xodimlar.append(ism)
        print(f"{ism} qo'shildi")

    def xodimlarni_chop_et(self):
        print(self.xodimlar)

menejer = Menejer("Akmal", "Jasur")

menejer.xodim_qosh("Sardor")
menejer.xodim_qosh("Komil")

menejer.xodimlarni_chop_et()
