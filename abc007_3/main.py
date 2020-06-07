import sys
import queue
from collections import deque
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    r, c = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    sy -= 1
    sx -= 1
    gy -= 1
    gx -= 1
    m = []
    costs = [[None for j in range(c)] for i in range(r)]
    for _ in range(r):
        m.append(list(input().strip()))
    q = deque()
    q.append((sy, sx, 0))
    costs[sy][sx] = 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while q:
        (y, x, cost) = q.popleft()
        if (y, x) == (gy, gx):
            print(cost)
            return
        for (add_y, add_x) in directions:
            new_y = y + add_y
            new_x = x + add_x
            if m[new_y][new_x] == '.' and costs[new_y][new_x] is None:
                costs[new_y][new_x] = cost + 1
                q.append((new_y, new_x, cost + 1))


if __name__ == '__main__':
    main()
