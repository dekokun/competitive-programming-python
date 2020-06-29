import sys
from collections import Counter
import math
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    n = int(input())
    mod = 10 ** 9 + 7
    l = [int(input()) for _ in range(n)]
    c = Counter(l)
    sumTime = 0
    penalty = 0
    for v in sorted(l):
        sumTime += v
        penalty += sumTime
    combi = 1
    for v in c:
        count = c[v]
        combi *= math.factorial(count)
        combi %= mod
    print(penalty)
    print(combi)


if __name__ == '__main__':
    main()
