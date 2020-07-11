import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    N, _L = map(int, input().rstrip().split())
    s = [input().rstrip() for _ in range(N)]
    print(''.join(sorted(s)))


if __name__ == '__main__':
    main()
