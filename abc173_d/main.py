import sys
import collections
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    n = int(input())
    a = map(int, input().rstrip().split())
    ans = 0
    candidates = collections.deque()
    for v in sorted(a, reverse=True):
        if not candidates:
            candidates.appendleft(v)
            continue
        if candidates[-1] > v:
            v2 = candidates.pop()
            ans += v2
            candidates.appendleft(v)
            candidates.appendleft(v)
        else:
            candidates.appendleft(v)
            ans += v
    print(ans)


if __name__ == '__main__':
    main()
