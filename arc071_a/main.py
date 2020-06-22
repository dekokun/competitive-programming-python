import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    n = int(input())
    ss = []
    for _ in range(n):
        ss.append(sorted(input().strip()))
    mapList = [dict() for _ in range(n)]
    for i in range(ord('a'), ord('z') + 1):
        c = chr(i)
        for j in range(len(ss)):
            s = ss[j]
            mapList[j][c] = 0
            for ch in s:
                if ch == c:
                    mapList[j][c] += 1
                else:
                    break
            ss[j] = ss[j][mapList[j][c]:]
    ans = ''
    for i in range(ord('a'), ord('z') + 1):
        c = chr(i)
        count = 100
        for map in mapList:
            count = min(count, map[c])
        ans += c * count
    print(ans)


if __name__ == '__main__':
    main()
