import re

rgx = re.compile(
    r"(100+1+|01)+"
)

def b1013():
    for _ in range(int(input())):
        if rgx.fullmatch(input()):
            print('YES')
        else:
            print('NO')
