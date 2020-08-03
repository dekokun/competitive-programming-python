import sys
import numpy as np
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    np.set_printoptions(threshold=20)
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        return
    cnt = 0
    now = 7
    while True:
        cnt += 1
        if now % K == 0:
            print(cnt)
            return
        now = now * 10 + 7
        now %= K


if __name__ == '__main__':
    main()
