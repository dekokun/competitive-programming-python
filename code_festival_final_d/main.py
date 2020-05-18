import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


a = int(input())
print("{} {}".format(a + 1, 2))
