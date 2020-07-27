import sys
import numpy as np
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    np.set_printoptions(threshold=20)
    A, B, C = map(int, input().rstrip().split())
    K = int(input())
    # A < B < C
    while A >= B:
        B *= 2
        K -= 1
    while B >= C:
        C *= 2
        K -= 1
    if K >= 0:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
