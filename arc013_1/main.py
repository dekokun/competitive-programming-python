from itertools import permutations
import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


a, b, c = map(int, input().split())
l = list(map(int, input().split()))
ans = 0
for i in permutations(range(3)):
    ans = max(ans, (a // l[i[0]]) * (b // l[i[1]]) * (c // l[i[2]]))
print(ans)
