class Turar_Joy:

    def __init__(self, manzil, xonalar_soni, ijara_xaqi):
        self.manzil = manzil
        self.xonalar_soni = xonalar_soni
        self.ijara_xaqi = ijara_xaqi

    def ijara_haqini_oshir(self, foiz):
        self.ijara_xaqi += self.ijara_xaqi * (foiz / 100)

    def malumotni_chop_et(self):
        print(f"Turar joyning ma'lumotlari: Manzil - {self.manzil}, Xonalar soni - {self.xonalar_soni}, Ijara puli - {self.ijara_xaqi} so'm")

turar_joy = Turar_Joy("Toshkent", 2, 1200)

turar_joy.ijara_haqini_oshir(20)

turar_joy.malumotni_chop_et()
