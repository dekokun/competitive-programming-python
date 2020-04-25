import sys
input = sys.stdin.readline

HIT, MISS, CENTER, WRONG = "HIT", "MISS", "CENTER", "WRONG"


def log(v):
    print(v, file=sys.stderr)


def output(v):
    print(v, flush=True)


def solve():
    check_line = 0
    # 右を取得
    left = 0
    right = 10**9 + 1
    while right - left > 1:
        mid = left + (right - left) // 2
        throw = "{} {}".format(mid, check_line)
        log(throw)
        output(throw)
        out = input().strip()
        if out == CENTER:
            return
        elif out == WRONG:
            exit(0)
        elif out == HIT:
            left = mid
        elif out == MISS:
            right = mid
    right_edge = left
    log("right {} {}".format(right_edge, check_line))
    # 左を取得
    left = -(10**9 + 1)
    right = 0
    while right - left > 1:
        mid = left + (right - left) // 2
        throw = "{} {}".format(mid, check_line)
        output(throw)
        out = input().strip()
        if out == CENTER:
            return
        elif out == WRONG:
            exit(0)
        elif out == HIT:
            right = mid
        elif out == MISS:
            left = mid
    left_edge = right
    log("left {} {}".format(left_edge, check_line))
    center_line = (left_edge + right_edge) // 2
    log("center {}".format(center_line))
    check_line = center_line
    # 上を取得
    left = 0
    right = 10**9 + 1
    while right - left > 1:
        mid = left + (right - left) // 2
        throw = "{} {}".format(check_line, mid)
        log(throw)
        output(throw)
        out = input().strip()
        if out == CENTER:
            return
        elif out == WRONG:
            exit(0)
        elif out == HIT:
            left = mid
        elif out == MISS:
            right = mid
    top_edge = left
    log("top {} {}".format(top_edge, check_line))
    # 下を取得
    left = -(10**9 + 1)
    right = 0
    while right - left > 1:
        mid = left + (right - left) // 2
        throw = "{} {}".format(check_line, mid)
        output(throw)
        out = input().strip()
        if out == CENTER:
            return
        elif out == WRONG:
            exit(0)
        elif out == HIT:
            right = mid
        elif out == MISS:
            left = mid
    bottom_edge = right
    log("bottom {} {}".format(bottom_edge, check_line))
    center_line2 = (top_edge + bottom_edge) // 2
    throw = "{} {}".format(center_line, center_line2)
    output(throw)
    log(throw)
    out = input().strip()
    if out == CENTER:
        return
    elif out == WRONG:
        exit(0)
    elif out == HIT:
        exit(1)
    elif out == MISS:
        exit(1)


T, A, B = map(int, input().split())
for t in range(1, T + 1):
    solve()
