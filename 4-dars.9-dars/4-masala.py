class Dokon:
    def __init__(self, nom, manzil):
        self.nom = nom
        self.manzil = manzil
        self.mahsulotlar = {}

    def mahsulot_qosh(self, mahsulot, narx):
        self.mahsulotlar[mahsulot] = narx
        print(f"{mahsulot} {narx} so'm narxda qo'shildi.")

dokon = Dokon("Supermarket", "Toshkent")

dokon.mahsulot_qosh("Non", 3000)
dokon.mahsulot_qosh("Sut", 7000)

print(dokon.mahsulotlar)
