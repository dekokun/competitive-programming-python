import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


A, B, C, D = map(int, input().split())
while True:
    C -= B
    if C <= 0:
        print('Yes')
        exit(0)
    A -= D
    if A <= 0:
        print('No')
        exit(0)
