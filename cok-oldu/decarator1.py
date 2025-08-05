"""def logla(func):
    def wrapper(*args,**kwargs):
        print(f"{func.__name__} çağırldı")
        return func(*args,**kwargs)
    return wrapper

@logla
def selamla():
    print("merhaba")

def salla():
    print("salla")

salla()
selamla()"""
"""
def tekrar(n):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for _ in range(n):
                func(*args,**kwargs)
        return wrapper
    return decorator

@tekrar(5)
def selam():
    print("merhaba")

selam()
"""

"""
from functools import wraps
def log(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"{func.__name__} cağrıldı")
        return func(*args,**kwargs)
    return wrapper

@log 
def selamla():
    print("merahba")

selamla(
"""
def add_repr(cls):
    cls.__repr__= lambda self: f"{cls.__name__}({self.__dict__})"
    return cls
@add_repr
class Araba:
    def __init__(self,marka):
        self.marka = marka

print(Araba("bmw"))