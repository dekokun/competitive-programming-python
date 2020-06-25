import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    _, k = map(int, input().strip().split())
    ps = sorted(map(int, input().strip().split()))
    print(sum(ps[:k]))


if __name__ == '__main__':
    main()
