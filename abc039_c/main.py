import sys
input = sys.stdin.readline


def log(v):
    print(v, file=sys.stderr)


from_first = "WBWBWWBWBWBWWBWBWWBWBWBW"

s = input()
first_five = s[0:11]

dictionary = {0: "Do", 2: "Re", 4: "Mi", 5: "Fa", 7: "So", 9: "La", 11: "Si"}

for i in range(0, 12):
    if from_first[i:i+11] == first_five:
        print(dictionary[i])
        exit(0)
exit(1)
