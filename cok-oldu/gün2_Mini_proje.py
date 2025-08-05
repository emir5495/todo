class Arac:
   def __init__(self,marka,plaka,sase_no):
     self.marka = marka
     self._plaka = plaka
     self.__sase_no = sase_no
   def haraket_et(self):
     print("harekete geçildi"),
   def __str__(self):
     return f"{self.marka} markalı aracın  plakası {self._plaka} şase nosu  {self.__sase_no}"
class Otomobil(Arac):
    def __init__(self,marka,plaka, sase_no,kapi_sayisi):
     super().__init__(marka,plaka,sase_no)
     self.kapi_sayisi = kapi_sayisi 
    def klima_ac(self):
     print(f"klima açılıyor {self.marka}")
class Kamyon(Arac):
   def __init__(self, marka, plaka, sase_no, yuk_kapasitesi):
     super().__init__(marka,plaka, sase_no)
     self.yuk_kapasitesi = yuk_kapasitesi
   def yuk_tasi(self):
     print("yük alındı")

oto1 = Otomobil("mercedenz", "34gs1905", "243r4rf3", 5)
print(oto1)
oto1.klima_ac()
