from collections import deque

inf = float('inf')

def b7569():
    M, N, H = map(int, input().split())
    li = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
    MAP = [[[inf for _ in range(M)] for _ in range(N)] for _ in range(H)]
    queue = deque()
    for i, ll in enumerate(li):
        for j, l in enumerate(ll):
            for k, x in enumerate(l):
                if x == 1:
                    MAP[i][j][k] = 0
                    queue.append((i, j, k))

    while queue:
        h, n, m = queue.popleft()
        v = MAP[h][n][m]
        for dm, dn, dh in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            x, y, z = m + dm, n + dn, h + dh
            if not (0 <= x < M and 0 <= y < N and 0 <= z < H): continue
            f = MAP[z][y][x]
            if li[z][y][x] != -1 and v + 1 < f:
                MAP[z][y][x] = v + 1
                queue.append((z, y, x))

    res = 0
    for i, ll in enumerate(MAP):
        for j, l in enumerate(ll):
            for k, x in enumerate(l):
                if li[i][j][k] != -1:
                    res = max(res, x)
    if res == inf: res = -1
    print(res)
