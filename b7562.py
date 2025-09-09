def b7562():
    for _ in range(int(input())):
        L = int(input())
        KX, KY = map(int, input().split())
        TX, TY = map(int, input().split())
        MAP = [[0]*L for _ in range(L)]
        que = [(KX, KY)]

        while len(que) != 0:
            x, y = que.pop(0)
            if (x, y) == (TX, TY): break
            for nx, ny in [
                (x + 2, y + 1), (x - 2, y + 1), (x + 2, y - 1), (x - 2, y - 1),
                (x + 1, y + 2), (x - 1, y + 2), (x + 1, y - 2), (x - 1, y - 2)
            ]:
                if nx < 0 or nx >= L or ny < 0 or ny >= L: continue
                if MAP[ny][nx]: continue
                MAP[ny][nx] = MAP[y][x] + 1
                que.append((nx, ny))

        print(MAP[TY][TX])