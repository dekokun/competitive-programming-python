import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    s = input().rstrip()
    t = input().rstrip()
    for i in range(len(t)):
        if s[i] == t[i]:
            continue
        if s[i] == '@' and t[i] in 'atcoder' or t[i] == '@' and s[i] in 'atcoder':
            continue
        else:
            print('You will lose')
            return
    print('You can win')


if __name__ == '__main__':
    main()
