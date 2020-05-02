from itertools import combinations
import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


N = int(input())
l = []
for _ in range(0, N):
    l.append(int(input()))
ans = []


def dfs(depth, a, b):
    if depth == N:
        ans.append(max(a, b))
    else:
        dfs(depth + 1, a + l[depth], b)
        dfs(depth + 1, a, b + l[depth])


dfs(0, 0, 0)
print(min(ans))
