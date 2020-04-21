import sys
input = sys.stdin.readline


def log(v):
    print(v, file=sys.stderr)


N, K = map(int, input().split())

mod = 10**9 + 7
log(mod)
ans = 0
for i in range(K, N + 2):
    max = (N - i + 1 + N) * i // 2
    min = (i - 1) * i // 2
    ans += max - min + 1
    ans %= mod
print(ans)
