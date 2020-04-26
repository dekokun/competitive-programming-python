import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


all = set()

N = int(input())
for _ in range(0, N):
    all.add(input())
print(len(all))
