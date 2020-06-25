import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    n, m = map(int, input().strip().split())
    board = [list(map(int, (input().rstrip()))) for _ in range(n)]
    ans = [[0] * m for _ in range(n)]
    for (i, row) in enumerate(board):
        for (j, cell) in enumerate(row):
            if cell != 0:
                board[i][j] = 0
                ans[i + 1][j] += cell
                board[i + 1][j - 1] -= cell
                board[i + 1][j + 1] -= cell
                board[i + 2][j] -= cell
    for row in ans:
        print("".join(map(str, row)))


if __name__ == '__main__':
    main()
