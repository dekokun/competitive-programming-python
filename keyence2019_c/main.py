import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    minus_sum = 0
    pluses = []
    ans = 0
    for i in range(n):
        if a[i] < b[i]:
            minus_sum += b[i] - a[i]
            ans += 1
        else:
            pluses.append(a[i] - b[i])
    pluses.sort(reverse=True)
    for v in pluses:
        if minus_sum <= 0:
            break
        minus_sum -= v
        ans += 1
    if minus_sum > 0:
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    main()
