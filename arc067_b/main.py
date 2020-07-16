import sys
import numpy as np
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    n, a, b = map(int, input().rstrip().split())
    x = list(map(int, input().rstrip().split()))
    ans = 0
    for diff in np.diff(x):
        if diff * a < b:
            ans += diff * a
        else:
            ans += b
    print(ans)


if __name__ == '__main__':
    main()
