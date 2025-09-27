def b1926():
    from collections import deque
    N, M = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    n, res = 0, 0

    for w in range(N * M):
        x, y = w % M, w // M
        if not MAP[y][x]: continue
        a = 1
        n += 1
        q, MAP[y][x] = deque([(x, y)]), 0
        while q:
            x, y = q.popleft()
            for xd, yd in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + xd, y + yd
                if nx < 0 or nx >= M: continue
                if ny < 0 or ny >= N: continue
                if not MAP[ny][nx]: continue
                MAP[ny][nx] = 0
                a += 1
                q.append((nx, ny))
        res = max(res, a)
    print(n, res, sep='\n')
