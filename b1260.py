def b1260():
    N, M, V = map(int, input().split())
    V -= 1
    li = [[] for _ in range(N)]
    MARK = [False for _ in range(N)]
    for _ in range(M):
        fr, to = map(int, input().split())
        li[fr - 1].append(to - 1)
        li[to - 1].append(fr - 1)
    for _ in range(N): li[_].sort()

    def dfs(here, mark = MARK.copy()):
        res = [here]
        mark[here] = True
        for i in li[here]:
            if mark[i]: continue
            res.extend(dfs(i, mark))
        return res

    mark = MARK.copy()
    mark[V] = True
    q, bfs = [V], []
    while q:
        me = q.pop(0)
        bfs.append(me)
        for i in li[me]:
            if mark[i]: continue
            mark[i] = True
            q.append(i)

    print(' '.join(map(str, [x + 1 for x in dfs(V)])))
    print(' '.join(map(str, [x + 1 for x in bfs])))
