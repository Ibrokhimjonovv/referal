# class Registration_form: #Registration_form degan class yaratdik
#     royxat  = {"Ali|Vali":'1234'} # class ichida lugatli yaratdik
#     def __init__(self) -> None: # obekt yaratsa boladi
#         pass # Hech narsa bo'lmaganligi uchun pass qoydik


#     ####################################
#     ########## CLASSMETHODLAR ##########
#     ####################################
#     @classmethod # classga tegishli metod
#     def check_pwd(self, p1, p2): # parol tekshirish uchun funksiya uni ichiga 2 ta argument berdik
#         if p1 == p2: # tekshiramiz agar p1 p2 ga teng bo'lsa
#             return True # True qiymat qaytar
#         else: #aks holda
#             return False # False qiymat qaytar

    
#     @classmethod # classga tegishli metod
#     def view(self, usr, id): # id ni tekshirish uchun view degan funksiya yaratib unga 2 ta argument berdik
#         if id == Registration_form.royxat[usr]['id']: # agar id royxat ichidagi id ga teng bo'lsa
#             print(f"Sizning parolingiz {(Registration_form.royxat[usr]['password'])}") # ekranga foydalanuvchini paroloni chiqaradi
#         else: # aks xolda 
#             print('Siz ushbu shaxs ekanligingizga shubxa bor') # <<< shu yozuvni ekranga chiqaradi 


#     @classmethod # classga tegishli metod
#     def msid(self): # msid nomli funksiya argument sifatida selfni o'zini beramiz
#         import random # random kutbxonasini chaqiramiz
#         uid = '' # bo'sh string ro'yxat 
#         for i in range(6):# i uchun 6 marta
#             uid += str(random.randint(0, 9)) # random randint yordamida 0 dan 9 gacha tasodifiy sonni tanlab uid ga stringga aylantirib qo'shib ketamiz
#         return uid # uid ni qaytaradi

    
    
#     ####################################
#     ############ METHODLAR #############
#     ####################################
#     def register(self, name, surname, pwd, pwd_again): # register nomli funksiya yaratib unga 4 ta argument beramiz
#         self.name = name # classga tegishli funksiya bo'lgani uchun self ga tengladik
#         self.surname = surname # classga tegishli funksiya bo'lgani uchun self ga tengladik
#         self.pwd = pwd # classga tegishli funksiya bo'lgani uchun self ga tengladik
#         self.pwd_again = pwd_again # classga tegishli funksiya bo'lgani uchun self ga tengladik
#         self.tekshiruv = Registration_form.check_pwd(self.pwd, self.pwd_again) # self.tekshiruv degan o'zgaruvchi olib unga check_pwd  metodini chaqirdik
#         self.full = f'{self.name}|{self.surname}' # self.full degan o'zgaruvchi yaratdik va unga name va surname argumentini yukladik
#         self.activate = Registration_form.msid() # self.active degan o'zgaruvchi yaratib unga msid() metodini yukladik
#         self.ijro = {'password':self.pwd,
#         'id':self.activate} # self.ijro degan lugat yaratdik
#         if self.tekshiruv and self.full not in list((Registration_form.royxat).keys()): # agar self.tekshiruv va self.full ro'yxat kalitlari ichida bo'lmasa
#             Registration_form.royxat[self.full] = self.ijro # royxatga self.fullni kalit self.ijroni qiymat sifatida yuklayapdi
#             print("Siz muvaffaqiyatli ro`yxatdan o`tdingiz") # <<< shu yozuvni ekranga ekranga chiqardi
#             print(f'Sining aktivatsiya kodinggiz {self.activate}') # ekranga self.active o'zgaruvchisini chaqirib qo'yyapmiz
#         elif self.tekshiruv == False: # aksincha self.tekshiruv  False qiymatga teng bolsa
#             print("Kiritgan parollaringiz bir biriga mos kelmadi") #<<< shu yozuvni ekranga chiqaradi
#         elif self.full in list((Registration_form.royxat).keys()): # aksincha self.full royxat kalitlari ichida bolsa
#             print('Siz oldin ro`yxatdan o`tgansiz') # <<< ekranga shu yozuvni chiqaradi
            
#         else: # aksincha
#             print("Kutilmagan hatolik ro`y berdi") # <<< shu yozuvni ekranga chiqaradi

    
    

#     def signin(self, username, passwd): # signin degan funksiya yaratib unga 2 ta argument beramiz
#         self.username = username # classga tegishli funksiya bo'lgani uchun self ga tengladik
#         self.passwd = passwd # classga tegishli funksiya bo'lgani uchun self ga tengladik
#         if self.username in list((Registration_form.royxat).keys()): # agar self.username royxat kalitlari ichida bolsa
#             if self.passwd == Registration_form.royxat[username]['password']: # agar self.passwd royxatdagi username qiymatiga teng bolsa
#                 print('Ishchi oynaga xush kelibsiz') #<<< ekranga shu yozuvni chiqaradi
#             else: # aksincha
#                 javob = input('Agar parolingiz esdan chiqqan bo`lsa, uni tiklash uchun 1 ni kiriting: ') #javob degan ozgaruvchiga input yuklaymiz
#                 if javob == '1': # agar javob 1 ga teng bolsa
#                     id = input('Aktivatsiya kodini kiriting: ') #id ga input yuklayapti
#                     Registration_form.view(self.username, id) # va classga tegishi bolgan metodni chaqiryapti





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

