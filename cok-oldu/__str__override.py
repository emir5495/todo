class Araba:
    def __init__(self,marka,hiz):
        self.marka = marka 
        self.hiz = hiz
    def __str__(self):
        return f"{self.marka} şu anda {self.hiz} km/s hızla gidiyor"
a = Araba("merco",120)
print(a)