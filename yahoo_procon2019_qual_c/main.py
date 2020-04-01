import sys
input = sys.stdin.readline
k, a, b = map(int, input().split())

# ずっと叩いたほうがいい場合
# bの方がaより小さかったら交換する意味がない
# aがb-1の場合、2回で1枚増えるより叩いて2回で2枚増えた方がお得
# a - 1回叩いてaになった時点で2回残ってないと交換できない
# 2回ないと交換できない
if a >= b or a == b - 1 or k < (a - 1) + 2 or k == 1:
    print(1 + k)
    exit(0)
# 叩いてa枚にする
k -= (a - 1)
ans = a
# ひたすら交換する
ans += (b - a) * (k // 2)
ans += k % 2
print(ans)
