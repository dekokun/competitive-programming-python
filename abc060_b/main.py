import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    A, B, C = map(int, input().strip().split())
    rems = set()
    for i in range(0, 101):
        v = (A * i) % B
        if v == C:
            print("YES")
            return
        if v in rems:
            print("NO")
            return
        rems.add(v)


if __name__ == '__main__':
    main()
