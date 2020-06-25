import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    ans = 1000000000
    _n = int(input())
    a = list(map(int, input().rstrip().split()))
    for i in range(-100, 101):
        tmp = 0
        for v in a:
            tmp += pow((v - i), 2)
        ans = min(tmp, ans)
    print(ans)


if __name__ == '__main__':
    main()
