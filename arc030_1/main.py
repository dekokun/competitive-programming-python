import sys
input = sys.stdin.readline


def main():
    n = int(input())
    k = int(input())
    if n - k >= k:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
