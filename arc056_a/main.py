import sys
# K 個のみかんを買うことが決まりました。 みかんは 1 個 A 円、さらに L 個のセットで B 円で売っています
A, B, K, L = map(int, input().split())
print(min((K // L) * B + (K - (K // L) * L) * A, ((K // L) + 1) * B))
