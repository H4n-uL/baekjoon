from collections import deque

inf = float('inf')

def b2206():
    N, M = map(int, input().split())
    li = [list(map(int, input())) for _ in range(N)]
    MAP = [[[None, None] for _ in range(M)] for _ in range(N)]
    MAP[0][0] = [1, None]
    queue = deque([(0, 0)])

    while queue:
        n, m = queue.popleft()
        v_nb, v_b = MAP[n][m]
        for dn, dm in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = n + dn, m + dm
            if not (0 <= x < N and 0 <= y < M): continue
            if v_nb != None and (z := MAP[x][y][li[x][y]] is None or z > v_nb + 1):
                MAP[x][y][li[x][y]] = v_nb + 1
            elif v_b != None and li[x][y] != 1 and (z := MAP[x][y][1] is None or z > v_b + 1):
                MAP[x][y][1] = v_b + 1
            else: continue
            queue.append((x, y))
    x, y = MAP[N - 1][M - 1]
    match x, y:
        case None, None: print(-1)
        case a, None: print(a)
        case None, b: print(b)
        case _: print(min(x, y))
