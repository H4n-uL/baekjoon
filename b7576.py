from collections import deque

inf = float('inf')

def b7576():
    N, M = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(M)]
    MAP = [[inf for _ in range(N)] for _ in range(M)]
    queue = deque()
    for i, l in enumerate(li):
        for j, x in enumerate(l):
            if x == 1:
                MAP[i][j] = 0
                queue.append((i, j))

    while queue:
        n, m = queue.popleft()
        v = MAP[n][m]
        for dn, dm in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = n + dn, m + dm
            if not (0 <= x < M and 0 <= y < N): continue
            z = MAP[x][y]
            if li[x][y] != -1 and v + 1 < z:
                MAP[x][y] = v + 1
                queue.append((x, y))

    res = 0
    for i, l in enumerate(MAP):
        for j, x in enumerate(l):
            if li[i][j] != -1:
                res = max(res, x)
    if res == inf: res = -1
    print(res)
