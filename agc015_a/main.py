import sys
input = sys.stdin.readline


def log(v):
    print(v, file=sys.stderr)


N, A, B = map(int, input().split())
maxNum = A + B * (N - 1)
minNum = A * (N - 1) + B
print(max(maxNum - minNum + 1, 0))
