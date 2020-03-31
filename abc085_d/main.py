import sys
input = sys.stdin.readline
# 振るの最強の剣の振ったダメージより強い投げるものを投げ続け、なくなったら振り続け、それを投げるよりも体力が減った段階で投げる
# フル強さが最強なのが複数あったら投げる強さが一番弱いやつを使う
n, h = map(int, input().split())
swords = []
for i in range(n):
    li = list(map(int, input().split()))
    li.insert(0, i)
    tu = tuple(li)
    swords.append(tu)
# 振るのが最強、投げるのはその中で最弱
sorted_by_slash = sorted(swords, key=lambda tu: (tu[1], -tu[2]))
max_slash = sorted_by_slash[len(sorted_by_slash) - 1]
sorted_by_throw = sorted(swords, key=lambda tu: tu[2])
sorted_by_throw.reverse()
hp = h
ans = 0
slash_damage = max_slash[1]
slash_id = max_slash[0]
for s in sorted_by_throw:
    throw_damage = s[2]
    id = s[0]
    # 振ると便利なやつは後にとっておく
    # TODO: 投げるだけで片のつく敵は投げた方が良い
    if slash_id == id:
        continue
    if slash_damage > throw_damage:
        break
    ans += 1
    hp -= throw_damage
    if hp <= 0:
        print(ans)
        exit()
# 振って最強の武器を投げた時の分を最後に投げる分を最初に計算しておく
ans += 1
hp -= max_slash[2]
if hp <= 0:
    print(ans)
    exit()

ans += ((hp - 1) // slash_damage) + 1

print(ans)
