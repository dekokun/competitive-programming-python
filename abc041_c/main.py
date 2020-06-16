import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = []
    for i in range(n):
        b.append((a[i], i + 1))
    for v in sorted(b, reverse=True):
        print(v[1])


if __name__ == '__main__':
    main()
