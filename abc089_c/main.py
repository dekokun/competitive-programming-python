import sys
from itertools import combinations
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    n = int(input().rstrip())
    m = {'M': 0, 'A': 0, 'R': 0, 'C': 0, 'H': 0}
    for _ in range(n):
        s = input().rstrip()
        if s[0] in m:
            m[s[0]] += 1
    ans = 0
    for c in combinations(m, 3):
        ans += m[c[0]] * m[c[1]] * m[c[2]]
    print(ans)


if __name__ == '__main__':
    main()
