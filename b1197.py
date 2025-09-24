import sys
sys.setrecursionlimit(10000)

def b1197():
    V, E = map(int, input().split())
    p = [-1] * V
    es = [tuple(map(int, input().split())) for _ in range(E)]
    es.sort(key = lambda x: x[2])

    def find(x) -> int:
        if p[x] < 0:
            return x
        p[x] = find(p[x])
        return p[x]

    def union(u, v) -> bool:
        u, v = find(u), find(v)
        if u == v: return False
        p[u] = v
        return True

    res = 0
    for a, b, c in es:
        if union(a - 1, b - 1): res += c
    print(res)