import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


K, T = map(int, input().split())
counts = map(int, input().split())
counts = sorted(counts, reverse=True)
print(max(0, counts[0] - (sum(counts) - counts[0]) - 1))
