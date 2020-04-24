import sys
input = sys.stdin.readline


def log(v):
    print(v, file=sys.stderr)


counts = dict()
N = int(input())
for _ in range(0, N):
    name = input().strip()
    if not name in counts:
        counts[name] = 0
    counts[name] += 1
for v in sorted(counts, key=counts.get, reverse=True):
    print(v)
    exit()
