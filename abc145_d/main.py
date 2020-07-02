import sys
from math import factorial
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    x, y = map(int, input().rstrip().split())
    # 全部 i + 1, j + 2が最初だったとする
    # a + 2b = x, 2a + b = y
    # =>
    # a = x - 2b
    # b = y - 2a
    # =>
    # b = y - 2x + 4b
    # 3b = 2x - y
    # b = (2x - y) / 3
    # a = (2y - x) / 3
    if (2 * x - y) % 3 != 0 or (2 * y - x) % 3 != 0:
        print(0)
        return
    a = (2 * x - y) // 3
    b = (2 * y - x) // 3
    if a < 0 or b < 0:
        print(0)
        return
    # (a + b) C min(a, b)
    # => (a + b)! / (min(a, b) ! * (a + b - min(a, b)) !
    mod = 10**9 + 7
    ans = (factorial_mod(a + b, mod) * pow(factorial_mod(min(a, b), mod), mod - 2, mod)
           * pow(factorial_mod(a + b - min(a, b), mod), mod - 2, mod)) % mod
    print(ans)


def factorial_mod(a, mod):
    ans = 1
    for v in range(1, a + 1):
        ans *= v
        ans %= mod
    return ans


if __name__ == '__main__':
    main()
