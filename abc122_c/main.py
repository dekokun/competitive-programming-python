import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    n, q = map(int, input().split())
    s = input().rstrip()
    before = ''
    start_cumsum = []
    now_val = 0
    for (i, c) in enumerate(s):
        if c == 'A':
            before = 'A'
        elif c == 'C' and before == 'A':
            now_val += 1
            before = ''
        else:
            before = ''
        start_cumsum.append(now_val)
    for _ in range(q):
        l, r = map(int, input().split())
        print(start_cumsum[r - 1] - start_cumsum[l - 1])


if __name__ == '__main__':
    main()
