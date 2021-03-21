# coding: utf-8
import bisect


class Baggage:
    def __init__(self, w, v):
        self.w = w
        self.v = v


def main():
    n, m, q = map(int, input().split())
    baggage_list = []
    for _ in range(n):
        w, v = map(int, input().split())
        baggage_list.append(Baggage(w, v))
    baggage_list = sorted(baggage_list, key=lambda x: x.v, reverse=True)

    x_list = list(map(int, input().split()))
    for _ in range(q):
        x_c = x_list.copy()
        l, r = map(int, input().split())
        del x_c[l-1:r]
        x_c.sort()

        sumv = 0
        for i in range(n):
            baggage = baggage_list[i]
            idx = bisect.bisect_left(x_c, baggage.w)
            if idx == len(x_c):
                continue
            x_c.pop(idx)
            sumv += baggage.v
        print(sumv)


if __name__ == '__main__':
    main()
