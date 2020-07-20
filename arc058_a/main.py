import sys
import numpy as np
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    np.set_printoptions(threshold=20)
    n, k = map(int, input().rstrip().split())
    ds = set(map(int, input().rstrip().split()))
    for i in range(n, 1000000):
        continue_flag = False
        for c in str(i):
            if int(c) in ds:
                continue_flag = True
        if continue_flag:
            continue
        else:
            print(i)
            return


if __name__ == '__main__':
    main()
