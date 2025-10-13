from collections import deque

def b16234():
    N, L, R = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    while True:
        bitmap = [[False] * N for _ in range(N)]
        z = False
        for rc in range(N*N):
            r, c = rc // N, rc % N
            if bitmap[r][c]: continue
            q, s = deque([(r, c)]), set()
            while q:
                r, c = q.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if nr in (-1, N) or nc in (-1, N): continue
                    if bitmap[nr][nc]: continue
                    if L <= abs(MAP[r][c] - MAP[nr][nc]) <= R:
                        s.add((nr, nc))
                        q.append((nr, nc))
                        bitmap[nr][nc] = True
                if len(s) == 0: break
                s.add((r, c))
                bitmap[r][c] = True
            if not s: continue
            z = True
            su, i = 0, len(s)
            for r, c in s: su += MAP[r][c]
            for r, c in s: MAP[r][c] = su // i

        if not z: break
        res += 1

    print(res)
