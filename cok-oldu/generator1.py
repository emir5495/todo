def sayac():
    for i in range(1,5):
        yield i

for x in sayac():
    print(x)