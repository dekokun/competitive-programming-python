import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    n = int(input().rstrip())
    ans = [0 for _ in range(n)]
    for x in range(1, 101):
        for y in range(x, 101):
            for z in range(y, 101):
                tmp = pow(x, 2) + pow(y, 2) + pow(z, 2) + x * y + y * z + z * x
                if tmp > n:
                    break
                if x == y == z:
                    ans[tmp - 1] += 1
                elif x == y or y == z or z == x:
                    ans[tmp - 1] += 3
                else:
                    ans[tmp - 1] += 6
    for v in ans:
        print(v)


if __name__ == '__main__':
    main()
