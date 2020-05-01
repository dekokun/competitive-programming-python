import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


N, M = map(int, input().split())
if N == 1 and M == 1:
    print(1)
    exit(0)
# Nは1じゃない状態
elif N == 1:
    N, M = M, N
if M == 1:
    print(N - 2)
    exit(0)

corner = 4
edge = (N - 2) * 2 + (M - 2) * 2

print(N * M - corner - edge)
