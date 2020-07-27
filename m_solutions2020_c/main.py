import sys
import numpy as np
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    np.set_printoptions(threshold=20)
    N, K = map(int, input().split())
    A = list(map(int, input().rstrip().split()))
    for i in range(K, N):
        log(A[i - K], A[i])
        if A[i - K] < A[i]:
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    main()
