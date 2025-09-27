def b1697():
    N, K = map(int, input().split())
    visited = [False] * 100001
    q, res = [N], 0
    visited[N] = True
    while K not in q:
        res += 1
        nq = []
        for n in q:
            if n - 1 >= 0 and not visited[n - 1]: nq.append(n - 1)
            if n + 1 < 100001 and not visited[n + 1]: nq.append(n + 1)
            if n << 1 < 100001 and not visited[n << 1]: nq.append(n << 1)
        q = nq
        for n in q: visited[n] = True
    print(res)
