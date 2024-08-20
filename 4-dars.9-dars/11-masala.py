class Xodim:
    def __init__(self, ism, lavozim, maosh):
        self.ism = ism
        self.lavozim = lavozim
        self.maosh = maosh
        self.bonuslar = {}  

    def bonus_qosh(self, oy, miqdor):
        self.bonuslar[oy] = miqdor

    def umumiy_maosh(self):
        bonus_summa = sum(self.bonuslar.values())
        return self.maosh * 12 + bonus_summa

    def yaxshi_xodim(self):
        if self.umumiy_maosh() > 1000000:
            return "Yaxshi xodim"
        else:
            return "Oddiy xodim"

xodim = Xodim("Ali", "Muhandis", 90000)

xodim.bonus_qosh("Yanvar", 50000)
xodim.bonus_qosh("Fevral", 30000)

umumiy_maosh = xodim.umumiy_maosh()
print(f"Umumiy yillik maosh: {umumiy_maosh}")

# Xodimning holatini tekshirish
holat = xodim.yaxshi_xodim()
print(holat)
