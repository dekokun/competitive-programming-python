s = list(input())
s.reverse()

odd = 0
even = 0

for i, v in enumerate(s):
    if i % 2 == 0:
        even += int(v)
    else:
        odd += int(v)
print('{} {}'.format(odd, even))
