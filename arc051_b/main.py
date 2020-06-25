import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    k = int(input().rstrip())
    a = 1
    b = 1
    for _ in range(k):
        a, b = b + a, a
    print("{} {}".format(a, b))


def gcd(a, b):
    return gcd_rec(a, b, 0)


def gcd_rec(a, b, counter):
    if b == 0:
        return a, counter
    counter += 1
    return gcd_rec(b, a % b, counter)


if __name__ == '__main__':
    main()
