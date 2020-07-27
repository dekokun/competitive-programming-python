import sys
import numpy as np
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    np.set_printoptions(threshold=20)
    A, K = map(int, input().rstrip().split())
    if K == 0:
        print(2 * pow(10, 12) - A)
        return
    now = A
    day = 0
    while now < 2 * pow(10, 12):
        day += 1
        now += 1 + K * now
    print(day)


if __name__ == '__main__':
    main()
