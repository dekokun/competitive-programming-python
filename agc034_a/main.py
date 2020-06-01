import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    N, A, B, C, D = map(int, input().split())
    log(N, A, B, C, D)
    S = input()
    if "##" in S[A-1:max(D, C)]:
        print("No")
        return
    if C < D:
        print("Yes")
        return
    log(S[B-2:D+1])
    if "..." in S[B-2:D+1]:
        print("Yes")
        return
    print("No")


if __name__ == '__main__':
    main()
