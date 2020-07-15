import sys
import numpy as np

input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    # np.set_printoptions(threshold=np.inf)
    N = pow(10, 5)
    is_prime = np.ones(N, dtype=bool)
    is_prime[:2] = False
    max = int(np.sqrt(N))
    for j in range(2, max + 1):
        if (is_prime[j]):
            is_prime[j*j::j] = False
    like_2017 = np.ones(N, dtype=bool)
    like_2017[:2] = False
    for i in range(2, N):
        if (i % 2 == 0):
            like_2017[i] = False
            continue
        if (not is_prime[i]):
            like_2017[i] = False
            continue
        if (not is_prime[(i + 1) // 2]):
            like_2017[i] = False
            continue

    cumsum = np.cumsum(like_2017)
    q = int(input())
    for _ in range(q):
        l, r = map(int, input().rstrip().split())
        print(cumsum[r] - cumsum[l - 1])


if __name__ == '__main__':
    main()
