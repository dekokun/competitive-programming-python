import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    (xa, xb, ya, yb, za, zb) = map(int, input().split())
    ya -= xa
    yb -= xb
    za -= xa
    zb -= xb
    log(ya, yb, )
    print(abs(ya * zb - yb * za) / 2)


if __name__ == '__main__':
    main()
