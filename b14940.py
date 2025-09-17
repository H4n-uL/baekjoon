def int_m1(x): return int(x) - 1

def b14940():
    N, M = map(int, input().split())
    MAP = [list(map(int_m1, input().split())) for _ in range(N)]
    origin = (0, 0)
    for n, line in enumerate(MAP):
        if 1 in line: origin = (n, line.index(1))
    que = [origin]

    while que:
        n, m = que.pop(0)
        for nn, mm in [(n + 1, m), (n - 1, m), (n, m + 1), (n, m - 1)]:
            if nn < 0 or nn >= N or mm < 0 or mm >= M: continue
            if (nn, mm) == origin: continue
            if MAP[nn][mm]: continue
            MAP[nn][mm] = MAP[n][m] + 1
            que.append((nn, mm))

    for n in range(len(MAP)):
        print(
            ' '.join(
                str(0 if MAP[n][m] == -1 else MAP[n][m] - 1)
                for m in range(len(MAP[n]))
            )
        )