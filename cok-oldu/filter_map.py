cube = lambda x: x**3

def fibonacci(n):
    fib = []
    a,b = 0,1
    for _ in range(n+1):
        fib.append(a)
        a,b = b,a+b
    return fib

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))