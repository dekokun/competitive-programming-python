import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


S, W = map(int, input().split())
if S > W:
    print("safe")
else:
    print("unsafe")
