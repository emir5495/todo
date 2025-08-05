class One:
    def __init__(self):
        print("üst sınıf oluştu")
    def selamla(self):
        print("merhaba")
class Two(One):
    def __init__(self):
        super().__init__()
        print("ikinci sınıf oluştu")
    def selamla(self):
        print("hello")
y = One()
print(y.selamla())
x = Two()
print(x.selamla())