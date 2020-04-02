import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
l.insert(0, 0)
l.append(0)
costs = []


def log(v):
    print(v, file=sys.stderr)


for l2 in [l[i:i+2] for i in range(0, len(l)-1, 1)]:
    costs.append(abs(l2[0] - l2[1]))
all_cost = sum(costs)
print(all_cost, file=sys.stderr)
for i in range(1, n+1):
    print(all_cost - (abs(l[i - 1] - l[i]) +
                      abs(l[i] - l[i + 1]) - abs(l[i - 1] - l[i + 1])))
