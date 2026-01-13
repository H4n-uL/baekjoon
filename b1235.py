def b1235():
    n = int(input())
    li = [input() for _ in range(n)]
    for i in range(1, len(li[0]) + 1):
        s = set(l[::-1][:i] for l in li)
        if len(s) == len(li): break

    print(i)
