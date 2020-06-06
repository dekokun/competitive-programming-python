import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    n = int(input())
    l = []
    for _i in range(0, n):
        weight = int(input())
        max_index = len(l)
        for i in range(len(l)):
            v = l[i]
            if v >= weight and max_index == len(l):
                max_index = i
            elif v >= weight and l[max_index] < weight:
                max_index = i
        if max_index == len(l):
            l.append(weight)
        else:
            l[max_index] = weight
    print(len(l))


if __name__ == '__main__':
    main()
