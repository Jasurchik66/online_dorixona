
# class Odam:
#     def __init__(self,ismi,yoshi,manzili):
#         self.ismi = ismi,
#         self.yoshi = yoshi,
#         self.manzili = manzili

#     def gapir(self):
#         print(f"Mening ismim {self.ismi}")


#     def yur(self,km):
#         print(f"Men{km} yurdim")
       

# class Manzil:
#     def __init__(self,kocha,tuman,viloyat,uyraqami):
#         self.kocha = kocha
#         self.tuman = tuman

        

# odam = Odam("jasurchik",19,"Qoqon")
# print(odam.ismi)

# odam.gapir()









# class Kitob:
#     def __init__(self,nom,muallif,sahifalar):
#         self.nom = nom,
#         self.muallif = muallif,
#         self.sahifalar = sahifalar

#     def gapir(self):
#         print(f"Kitobnig nomi {self.nom}\nkitobnig muallifi{self.muallif}\nkitobning sahifasi {self.sahifalar}")
       
        

# kitob = Kitob("Hamsa","Alisher Navoiy",5000)
# # print(kitob.nom,kitob.muallif,kitob.sahifalar)

# kitob.gapir()









# class Odam:
#     def __init__(self,ismi,yoshi,manzili):
#         self.ismi = ismi,
#         self.yoshi = yoshi,
#         self.manzili = manzili

#     def gapir(self):
#         print(f"Mening ismim {self.ismi}")


#     def yur(self,km):
#         print(f"Men{km} yurdim")
       

        

# odam = Odam("jasurchik",19,"Qoqon")


# odam.gapir()

# class Student(Odam):
#     def __init__(self, ismi, yoshi, manzili,univeri,kursi,guruhi):
#         super().__init__(ismi, yoshi, manzili)
#         self.univeri = univeri
#         self.kursi = kursi
#         self.guruhi = guruhi

#     def referat(self,fan):
#         print(f"Men {fan} dan referat qildim")


# student = Student("Jasurchik",19,"Qoqon","TATU",2,"FN27")

# student.referat("Matematika")



# class Kitob:
#     def __init__(self,nomi,muallifi,beti):
#         self.nomi = nomi
#         self.muallifi = muallifi
#         self.beti = beti
    

# class ElektronKitob(Kitob):
#     def __init__(self, nomi, muallifi, beti,formati,hajmi):
#         super().__init__(nomi, muallifi, beti)
#         self.formati = formati
#         self.hajmi = hajmi
    

#     def malumot_ber(self):
#         print(f"{self.nomi}\n{self.muallifi}")

# class BosmaKitob(Kitob):
#     def __init__(self, nomi, muallifi, beti,muqovasi,qogoz):
#         super().__init__(nomi, muallifi, beti)
#         self.muqovasi = muqovasi
#         self.qogoz = qogoz

# e_atom_odatlar = ElektronKitob("Atom odatlar","Alisher",230,"pdf","2MB")
# molxona = BosmaKitob("Molxona","Jorj",300,"Yumshoq","oq")

# e_atom_odatlar.malumot_ber()











# class Cars:
#     def __init__(self, nomi, raqami, yili):
#         self.nomi = nomi
#         self.raqami = raqami
#         self.yili = yili

#     def malumot_ber(self):
#         print(f"Mashinaning nomi: {self.nomi}\nMashina raqami: {self.raqami}\nYili: {self.yili}")

# class SportCar(Cars):
#     def __init__(self, nomi, raqami, yili, tezlanishi, narxi):
#         super().__init__(nomi, raqami, yili)
#         self.tezlanishi = tezlanishi
#         self.narxi = narxi

# class YukCar(Cars):
#     def __init__(self, nomi, raqami, yili, yuk, ogirligi):
#         super().__init__(nomi, raqami, yili)
#         self.yuk = yuk
#         self.ogirligi = ogirligi


# car = SportCar("BMV", 777, 2024, 3.5, 100000)


# car.malumot_ber()











# import random

# class BankHisobi:
#     def __init__(self, mijoz_ismi, balans=0.0):
#         self.hisob_raqami = random.randint(10000000000000000, 1000000000000000000000)
#         self.mijoz_ismi = mijoz_ismi
#         self.balans = balans

#     def pul_qosh(self, miqdor):
#         self.balans += miqdor

#     def pul_yech(self, miqdor):
#         if miqdor>self.balans:
#            print("Yetarli mablag' yo'q!!!")
#            return
#         self.balans -= miqdor

#     def malumotni_chop_et(self):
#         print(f"""
#         Hisob raqami: {self.hisob_raqami}
#         Ismi: {self.mijoz_ismi}
#         Balans: {self.balans}
#     """)

# class Bank:
#     def __init__(self, hisob_raqamlar_listi=[]):
#         self.hisob_raqamlar_listi = hisob_raqamlar_listi

#     def yangi_hisob_raqam_qoshish(self):
#         mijoz_ismi = input("Mijoz ismini kirit: ")
#         balansi = float(input("Dastlabki mablagi: "))

#         hisob = BankHisobi(mijoz_ismi, balansi)
#         self.hisob_raqamlar_listi.append(hisob)

#     def barcha_hisoblar(self):
#         for hisob in self.hisob_raqamlar_listi:
#             hisob.malumotni_chop_et()
#             print("######################")

#     def qidirish(self, ismi):
#         for hisob in self.hisob_raqamlar_listi:
#             if hisob.mijoz_ismi == ismi:
#                 print("######################")
#                 hisob.malumotni_chop_et()

#     def pul_qosh(self,hisob_raqami,amount):
#         hisoblar = list(filter(lambda hisob:hisob_raqami == self.hisob_raqamlar_listi))
#         if len(hisoblar)>=1:
#             hisoblar[0].pul_qosh(amount)

    
#     def pul_yech(self, hisob_raqami, miqdor):
#         hisoblar = list(filter(lambda hisob: hisob.hisob_raqami == hisob_raqami, 
#          self.hisob_raqamlar_listi))
#         if len(hisoblar) >= 1:
#            hisoblar[0].pul_yech(miqdor)
       




# hisoblar = []
# hisoblar.append(BankHisobi("Akmal", 200))
# hisoblar.append(BankHisobi("Aziz", 300))
# hisoblar.append(BankHisobi("Anvar", 500))

# bank = Bank(hisoblar)

# while True:
#     print("1. Hisob raqam qoshish")
#     print("2. Hisob raqam qidirish")
#     print("3. Pul qoshish")
#     print("4. Pul yechish")
#     print("5. Barcha hisoblarni korish")
#     print("0. To'xtatish")

#     buyruq = int(input("Buyruqni tanla: "))

#     if buyruq == 1:
#         bank.yangi_hisob_raqam_qoshish()
#     if buyruq == 2:
#         ismi = input("Mijoz ismini kirit: ")
#         bank.qidirish(ismi)
#     if buyruq == 3:
#         raqami = int(input("raqami kirit :"))
#         miqdori = float(input("Qancha qoshasz :"))
#         bank.pul_qoshish(raqami,miqdori)

#     if buyruq == 4:
#          raqami = int(input("Hisob raqamini kiriting: "))
#          miqdor = float(input("Yechildigan mablag': "))
#          bank.pul_yech(raqami, miqdor)

#     if buyruq == 5:
       
#         bank.barcha_hisoblar()

#     if buyruq == 0:
#         break











# class Person:
#     def __init__(self, ism="", familiya="", yosh=""):
#         self.ism = ism
#         self.familiya = familiya
#         self.yosh = yosh


# def __str__(self):
#     print(f"{self.ism}{self.familiya}{self.yosh}")


# if __name__ == "__main__":
#     ism = input("Ismingizni kiriting: ")
#     familiya = input("Familiyangizni kiriting: ")
#     yosh = int(input("Yoshingizni kiriting: "))

#     pr = Person(ism, familiya, yosh)
#     print(f"Ism: {pr.ism}, Familiya: {pr.familiya}, Yosh: {pr.yosh}")





class Student:
    def __init__(self, name, sr, age, ID, guruh_name):
        self.name = name
        self.surname = sr
        self.age = age
        self.ID = ID
        self.guruh_name = guruh_name
        self.grades = list()

    def add_grade(self, grade) -> None:
        self.grades.append

    def edit_student(self,nm, sur, br, gr_name):
        self.name = nm
        self.surname = sur
        self.age = br
        self.guruh_name = gr_name

   

    def __str__(self) -> str:
        return f"{self.name} {self.surname} {self.age} {self.guruh_name}"


class StudentManager:
    def __init__(self) -> None:
        self.list_students = []

    def add_students(self,student:Student):
        self.list_students.append(student)
        
   


   
if __name__ == "__main__":
    st = Student ("Hasanboy","Maqsudaliyev",18,65165165,"FN27")
    print(st)

    st.edit_student("Jasurbek","Yodgorov",19,"FN23")
    print(st)





