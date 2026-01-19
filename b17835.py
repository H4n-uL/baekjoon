from collections import deque

def b17835():
    N, M, _ = map(int, input().split())
    d = [[] for _ in range(N)]
    for _ in range(M):
        u, v, c = map(int, input().split())
        d[v - 1].append((u - 1, c))

    res = [float('inf') for _ in range(N)]
    m = map(int, input().split())
    deq = deque((k - 1, 0) for k in m)
    for i, _ in deq: res[i] = 0

    while deq:
        p, c = deq.popleft()
        for px, cx in d[p]:
            if c + cx >= res[px]: continue
            res[px] = c + cx
            deq.append((px, c + cx))

    print(res.index(max(res)) + 1)
    print(max(res))
