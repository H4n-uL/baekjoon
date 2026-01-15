def b31264():
    _, M, A = map(int, input().split())
    li = sorted(map(int, input().split()))

    base = min(li)
    while True:
        t, f = base, 0
        for _ in range(M):
            x = max(i for i in li if i <= t)
            t += x
            f += x

        if f >= A:
            break

        base += 1

    print(base)
