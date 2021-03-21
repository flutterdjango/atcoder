# coding: utf-8
import itertools
import numpy as np


def main():
    n, k = map(int, input().split())
    patterns = list(itertools.permutations(range(1, n), n-1))

    costs = [list(map(int, input().split())) for _ in range(n)]
    costs = np.array(costs)

    cnt = 0
    for pattern in patterns:
        pattern = list(pattern)
        pattern.insert(0, 0)
        pattern.append(0)

        sumv = 0
        for i in range(len(pattern) - 1):
            start_idx = pattern[i]
            end_idx = pattern[i+1]
            sumv += costs[start_idx][end_idx]
        if sumv == k:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
