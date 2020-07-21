import sys
import numpy as np
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    np.set_printoptions(threshold=20)
    N = int(input())
    A = list(map(int, input().rstrip().split()))
    A.sort()
    ans = 1
    for v in A:
        ans *= v
        if ans > pow(10, 18):
            ans = -1
            break
    print(ans)


if __name__ == '__main__':
    main()
