import sys
import numpy as np
from datetime import datetime
from datetime import timedelta
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    np.set_printoptions(threshold=20)
    S = input().rstrip()
    date = datetime.strptime(S, "%Y/%m/%d")
    for i in range(0, 1000000000):
        added = date + timedelta(i)
        if added.year % (added.day * added.month) == 0:
            print(added.strftime("%Y/%m/%d"))
            return


if __name__ == '__main__':
    main()
