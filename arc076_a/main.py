import sys
import math
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    n, m = map(int, input().rstrip().split())
    if abs(n - m) >= 2:
        print("0")
        return
    if n == m:
        print(math.factorial(n) * math.factorial(m) * 2 % (pow(10, 9) + 7))
    else:
        print(math.factorial(n) * math.factorial(m) % (pow(10, 9) + 7))


if __name__ == '__main__':
    main()
