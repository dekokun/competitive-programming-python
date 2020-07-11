import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    s = input().rstrip()
    ans = 0
    for (i, c) in enumerate(s):
        if c == 'U':
            ans += len(s) - i - 1
            ans += 2 * i
        else:
            ans += (len(s) - i - 1) * 2
            ans += i
    print(ans)


if __name__ == '__main__':
    main()
