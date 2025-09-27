def int_m1(x): return int(x) - 1

def b2178():
    N, M = map(int, input().split())
    MAP = [list(map(int_m1, input())) for _ in range(N)]
    BITMAP = [[MAP[i][j] != 0 for j in range(M)] for i in range(N)]
    que = [(0, 0)]
    BITMAP[0][0] = True

    while len(que) != 0:
        x, y = que.pop(0)
        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if nx < 0 or nx >= M or ny < 0 or ny >= N: continue
            if BITMAP[ny][nx]: continue
            BITMAP[ny][nx] = True
            que.append((nx, ny))
            MAP[ny][nx] = MAP[y][x] + 1

    print(MAP[N - 1][M - 1] + 1)
