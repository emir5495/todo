#bu bir _protected örneğidir

class Kisi:
    def __init__(self, ad, soyad):
        self.ad = ad
        self._soyad = soyad
k = Kisi("emir","turgut")
print(k._soyad)

