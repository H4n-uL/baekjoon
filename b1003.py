d = dict()

def fibo(n: int) -> tuple[int, int]:
    if n == 0: return 1, 0
    elif n == 1: return 0, 1
    else:
        m1 = d.get(n - 1, None)
        if not m1: d[n - 1] = m1 = fibo(n - 1)
        m2 = d.get(n - 2, None)
        if not m2: d[n - 2] = m2 = fibo(n - 2)
        z1, o1 = m1
        z2, o2 = m2
        return z1 + z2, o1 + o2

def b1003():
    for _ in range(int(input())):
        print(*fibo(int(input())))
