import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    n = int(input())
    al = []
    bl = []
    for _ in range(n):
        a, b = map(int, input().split())
        al.append(a)
        bl.append(b)
    ans = 0
    for (i, a) in reversed(list(enumerate(al))):
        b = bl[i]
        a += ans
        a = a % b
        if a == 0:
            continue
        ans += b - a
    print(ans)


if __name__ == '__main__':
    main()
