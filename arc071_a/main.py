import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    n = int(input())
    l = []
    for _ in range(n):
        l.append(sorted(input().strip()))
    for c in range(ord('a'), ord('z') + 1):
        log(chr(c))
        # それぞれのリストにどの数がなんぼあるかを数える
    for c in range(ord('a'), ord('z') + 1):
        # それぞれの文字が最低何文字あるかを数える
        # 連結する


if __name__ == '__main__':
    main()
