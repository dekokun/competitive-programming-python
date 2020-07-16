import sys
from collections import defaultdict
import numpy as np
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    np.set_printoptions(threshold=20)
    n = int(input())
    a = [*map(int, input().rstrip().split())]
    m = defaultdict(int)
    for v in np.append(np.cumsum(a), 0):
        m[v] += 1
    ans = 0
    for key in m:
        v = m[key]
        if v > 1:
            ans += v * (v - 1) // 2
    print(ans)


if __name__ == '__main__':
    main()
