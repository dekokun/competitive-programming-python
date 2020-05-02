from itertools import combinations
import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


N = int(input())
l = []
l = [int(input()) for _ in range(N)]
ans = []


def dfs(depth, a, b):
    if depth == N:
        ans.append(max(a, b))
    else:
        dfs(depth + 1, a + l[depth], b)
        dfs(depth + 1, a, b + l[depth])


dfs(0, 0, 0)
print(min(ans))
