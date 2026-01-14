def b1283():
    ls = [input() for _ in range(int(input()))]
    d = dict()
    for kw in ls:
        klow = kw.lower()
        w = None

        for i, fw in enumerate(klow.split()):
            if not len(fw): continue
            if not d.get(fw[0]):
                fkw = ''.join(a + ' ' for a in klow.split()[:i])
                w = (fw[0], len(fkw))
                break

        if w:
            d[w[0]] = kw, w[1]
            continue

        for i, lt in enumerate(klow):
            if lt.isalpha() and not d.get(lt):
                w = (lt, i)
                break

        if w: d[w[0]] = kw, w[1]

    dx = {w: (k, i) for k, (w, i) in d.items()}

    for w in ls:
        ki = dx.get(w)
        if not ki:
            print(w)
            continue

        _, i = ki
        print(f'{w[:i]}[{w[i]}]{w[i+1:]}')
