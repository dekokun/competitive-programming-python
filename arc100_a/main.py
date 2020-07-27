import sys
import numpy as np
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    np.set_printoptions(threshold=20)
    N = int(input())
    l = list(map(int, input().rstrip().split()))
    for i, v in enumerate(l):
        l[i] = v - (i + 1)
    l.sort()
    now = 0
    for v in l:
        now += abs(v - (l[0] - 1))
    right_count = N
    left_count = 0
    ans = now
    before = l[0] - 1
    for v in l:
        now -= right_count * (v - before)
        now += left_count * (v - before)
        right_count -= 1
        left_count += 1
        ans = min(now, ans)
        before = v
    print(ans)


if __name__ == '__main__':
    main()
