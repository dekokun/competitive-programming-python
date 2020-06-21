import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    a = input().strip()
    if ord(a) < ord('a'):
        print('A')
    else:
        print('a')


if __name__ == '__main__':
    main()
