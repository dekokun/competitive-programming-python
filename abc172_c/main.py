import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    _n, _m, k = map(int, input().split())
    ns = list(map(int, input().rstrip().split()))
    ms = list(map(int, input().rstrip().split()))
    sum = 0
    count = 0
    for v in ns:
        if sum + v > k:
            break
        else:
            sum += v
            count += 1

    ans_now = count
    ans = ans_now
    i = count - 1
    for v in ms:
        if sum + v > k:
            while sum + v > k:
                if i < 0:
                    break
                sum -= ns[i]
                i -= 1
                ans_now -= 1
            if sum + v > k:
                break
            sum += v
            ans_now += 1
        else:
            sum += v
            ans_now += 1
        ans = max(ans, ans_now)
    print(ans)


if __name__ == '__main__':
    main()
