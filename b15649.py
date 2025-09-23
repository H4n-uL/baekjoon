def b15649(n, m, a=[], b=[]):
    if not b: b = [str(i+1) for i in range(n)]
    if len(a) == m: print(' '.join(a)); return
    for i in range(len(b)): b15649(n, m, a + [b[i]], b[:i] + b[i+1:])

if __name__ == '__main__':
    N, M = map(int, input().split())
    b15649(N, M)