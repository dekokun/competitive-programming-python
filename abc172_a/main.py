import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    a = int(input())
    print(a + a ** 2 + a ** 3)


if __name__ == '__main__':
    main()
