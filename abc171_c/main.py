import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    n = int(input().strip())
    ans = ''
    while n != 0:
        if n % 26 == 0:
            ans = 'z' + ans
            n -= 26
            n = n // 26
        else:
            ans = chr(n % 26 + ord('a') - 1) + ans
            n = n // 26
    print(ans)


if __name__ == '__main__':
    main()
