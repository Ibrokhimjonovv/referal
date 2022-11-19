
class Foydalanuvchi():
    royxat = {}
    referal = 0
    def __init__(self) -> None:
        pass
    
    @classmethod
    
    def register(self):
        import random
        tasodif = []
        for i in range(9):
            tasodif.append(i)
        aralash = random.shuffle(len(tasodif))
        print(aralash)
        ism = input("Ism kiriting: ").capitalize()
        familiya = input("Familiyani kiriting: ").capitalize()
        parol = input("Parolni kiriting: ")
        referal = input("Referal codingiz bormi (ha/yoq) ").lower()
        if referal =='ha':
            referal2 = input("Referal codni yozing: ")
            print("Referal code qabul qilindi")
        else:
            pass
        if f"{ism} {familiya}" not in list((Foydalanuvchi.royxat).keys()):
            Foydalanuvchi.royxat[f"{ism} {familiya}"] = parol
            print(f"Ro'yxatdan muvaffaqiyatli o'tdingiz\nSizning referal codingiz: {tasodif}")
        elif f"{ism} {familiya}" in list((Foydalanuvchi.royxat).keys()):
            print("Bu foydalanuvchi ro'yxatdan o'tgan")

q = Foydalanuvchi()
q.register()

