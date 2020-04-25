import sys
input = sys.stdin.readline


def log(v):
    print(v, file=sys.stderr)


def output(v):
    print(v, flush=True)


def solve():
    for i in range(-5, 6):
        for j in range(-5, 6):
            throw = "{} {}".format(i, j)
            log(throw)
            output(throw)
            out = input().strip()
            if out == "CENTER":
                log("PASS")
                return
            elif out == "WRONG":
                log("WRONG")
                return


T, A, B = map(int, input().split())
for t in range(1, T + 1):
    solve()
