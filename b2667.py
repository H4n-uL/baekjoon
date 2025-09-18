def b2667():
    from collections import deque
    MAP = [list(map(int, input())) for _ in range(int(input()))]
    n, apt = len(MAP), []

    for w in range(n * n):
        x, y = w % n, w // n
        if not MAP[y][x]: continue
        apt.append(1)
        q, MAP[y][x] = deque([(x, y)]), 0
        while q:
            x, y = q.popleft()
            for xd, yd in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + xd, y + yd
                if nx < 0 or nx >= n: continue
                if ny < 0 or ny >= n: continue
                if not MAP[ny][nx]: continue
                MAP[ny][nx] = 0
                apt[-1] += 1
                q.append((nx, ny))
    print(len(apt), *sorted(apt), sep='\n')