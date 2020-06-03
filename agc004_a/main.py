import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    l = list(map(int, input().split()))
    l = sorted(l)
    small = l[2] // 2
    large = l[2] - small
    print((large - small) * l[0] * l[1])


if __name__ == '__main__':
    main()
