import sys
import numpy as np
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    np.set_printoptions(threshold=20)
    n = int(input())
    if n % 2 == 1:
        print("")
        return
    for s in dfs("", [], n):
        print(s)


def dfs(first, stack, length):
    if len(first) + len(stack) >= length:
        stack.reverse()
        return [first + "".join(stack)]
    stack1 = stack.copy()
    stack1.append(')')
    a = dfs(first + '(', stack1, length)
    if not len(stack) == 0:
        next = stack.pop()
        a = a + dfs(first + next, stack, length)
    return a


if __name__ == '__main__':
    main()
