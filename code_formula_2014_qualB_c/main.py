from itertools import combinations
from itertools import product
import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    A = input().strip()
    B = input().strip()
    z = zip(A, B)
    before = []
    after = []
    for (a, b) in z:
        if a == b:
            continue
        before.append(a)
        after.append(b)
        if len(before) > 6:
            print("NO")
            return
    if len(before) == 0:
        if len(A) == len(set(A)):
            print("NO")
            return
        else:
            print("YES")
            return

    # beforeが1個だけのときどうなる？j
    for a in product(combinations(range(len(before)), 2), repeat=3):
        tmp = before.copy()
        for v in a:
            tmp[v[0]], tmp[v[1]] = tmp[v[1]], tmp[v[0]]
        if after == tmp:
            print("YES")
            return
    print("NO")
    return


if __name__ == '__main__':
    main()
