import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    l = input().strip()
    i = int(input().strip())
    print(l[i - 1])


if __name__ == '__main__':
    main()
