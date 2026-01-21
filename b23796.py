rot0   = lambda m: m
rotr90 = lambda m: [*map(list, zip(*m[::-1]))]
rotl90 = lambda m: [*map(list, zip(*m))][::-1]
rot180 = lambda m: [r[::-1] for r in m[::-1]]

def b23796():
    m = [list(map(int, input().split()))for _ in range(8)]
    d = {'U': (rotl90, rotr90), 'D': (rotr90, rotl90), 'R': (rot180, rot180), 'L': (rot0, rot0)}
    f, nf = d[input()]

    m, nm = f(m), []

    for l in m:
        x = set()
        for i in range(1, len(l)):
            if l[i] == 0: continue

            j = i
            for k in range(i - 1, -1, -1):
                j = k
                if l[j] != 0: break

            if l[j] == l[i] and j not in x:
                l[j] <<= 1
                x.add(j)
            elif l[j]:
                if j + 1 == i: continue
                l[j + 1] = l[i]
            else:
                l[j] = l[i]

            l[i] = 0
        nm.append(l)

    for l in nf(nm):
        print(*l)
