import sys
from collections import Counter
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    n = int(input())
    s = []
    for _ in range(n):
        s.append(input().rstrip())
    c = Counter(s)
    for s in ["AC", "WA", "TLE", "RE"]:
        print("{} x {}".format(s, c[s]))
   


if __name__ == '__main__':
    main()
