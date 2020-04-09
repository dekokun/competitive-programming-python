import sys
input = sys.stdin.readline


def log(v):
    print(v, file=sys.stderr)


N, K = map(int, input().split())
all_count = pow(N, 3)
# 中央値がKじゃない時を以下で列挙：
other_k = []
# Kが1個もない
other_k.append(pow(N - 1, 3))
# K以外の数字が2個あり、残りはK(残りがK以外は上のKが1個もないに含まれる)
other_k.append(3 * (pow(N - 1, 1)))
# Kが1個あるが残り2つが別の数でKより大きい(残り2つが同じの場合は上に含まれる)
other_k.append(3 * (N - K) * (N - K - 1))
# Kが1個あるが残り2つが別の数でKより小さい
other_k.append(3 * (K - 1) * (K - 2))
print((pow(N, 3) - sum(other_k))/pow(N, 3))
