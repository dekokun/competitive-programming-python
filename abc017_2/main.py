import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


s = input().strip()
search = ["o", "k", "u"]
ss = list(s)
before_c = False
for i in range(0, len(ss)):
    if before_c and ss[i] == 'h':
        before_c = False
        continue
    if ss[i] == 'c' and not before_c:
        before_c = True
        continue
    else:
        if ss[i] in search:
            continue
    print("NO")
    exit(0)
print("YES")
