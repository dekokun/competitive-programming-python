import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    n, m = map(int, input().strip().split())
    if m > n:
        print("NO")
        return
    a_s = sorted(list(map(int, input().strip().split())), reverse=True)
    b_s = sorted(list(map(int, input().strip().split())), reverse=True)
    for i in range(m):
        if a_s[i] < b_s[i]:
            print("NO")
            return
    print("YES")


if __name__ == '__main__':
    main()
