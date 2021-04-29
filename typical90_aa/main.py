import sys
import numpy as np
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    np.set_printoptions(threshold=20)
    n = int(input())
    se = set()
    for i in range(1, n + 1):
        s = input()
        if not s in se:
            print(i)
        se.add(s)


if __name__ == '__main__':
    main()
