class Tadbirkor:
    def __init__(self, ism, loyiha_soni):
        self.ism = ism
        self.loyiha_soni = loyiha_soni
        self.foyda = {}

    def foyda_qosh(self, loyiha, miqdor):
        if loyiha in self.foyda:
            self.foyda[loyiha] += miqdor
        else:
            self.foyda[loyiha] = miqdor

    def umumiy_foyda(self):
        return sum(self.foyda.values())

    def yaxshi_tadbirkor(self):
        if self.umumiy_foyda() > 5000000:
            return "Yaxshi tadbirkor"
        else:
            return "Oddiy tadbirkor"

tadbirkor = Tadbirkor("Olim", 3)

tadbirkor.foyda_qosh("Loyiha 1", 2000000)
tadbirkor.foyda_qosh("Loyiha 2", 3500000)
tadbirkor.foyda_qosh("Loyiha 3", 1000000)

print(f"Umumiy foyda: {tadbirkor.umumiy_foyda()} so'm")
print(tadbirkor.yaxshi_tadbirkor())
