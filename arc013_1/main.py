import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


N, M, L = map(int, input().split())
P, Q, R = map(int, input().split())
print(max((N//P) * (M//Q) * (L//R), (N//Q) *
          (M//R) * (L//P), (N//R) * (M//P) * (L//Q), (N//P) * (L//Q) * (M//R), (N//Q) *
          (L//R) * (M//P), (N//R) * (L//P) * (M//Q)))
