import sys

def log(v):
    print(v, file=sys.stderr)

N = int(input())
input_string = input()
chars = ['A', 'B', 'X', 'Y']
ans = 10000
for i in range(0, 4):
    for j in range(0, 4):
        for k in range(0, 4):
            for l in range(0, 4):
                commands = []
                commands.append(chars[i] + chars[j])
                commands.append(chars[k] + chars[l])
                before_char = ''
                now_ans = 0
                for c in input_string:
                    string = before_char + c
                    before_char = c
                    now_ans += 1
                    if string in commands:
                        before_char = ''
                        now_ans -= 1
                ans = min(ans, now_ans)
print(ans)
