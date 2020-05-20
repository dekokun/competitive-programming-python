import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


n = int(input())
l = map(int, input().split())

four_count = 0
two_count = 0
for v in l:
    if v % 4 == 0:
        four_count += 1
    elif v % 2 == 0:
        two_count += 1

if two_count > 0:
    if n - two_count - four_count <= four_count:
        print("Yes")
    else:
        print("No")
else:
    if n - four_count - 1 <= four_count:
        print("Yes")
    else:
        print("No")
