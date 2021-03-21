# coding: utf-8

def is_possible(k: int, s: list, t: list) -> bool:
    for i in range(1, 10):
        if s.count(i) + t.count(i) > k:
            return False
    return True


def calc_point(k: int, s: list) -> int:
    sumv = 0
    for i in range(1, 10):
        sumv += i * 10 ** s.count(i)
    return sumv


def get_remain_cards(s, t, sealed_i, sealed_j):
    s_c = s.copy()
    t_c = t.copy()
    s_c.append(sealed_i)
    t_c.append(sealed_j)


def main():
    k = int(input())
    s = list(input())
    t = list(input())
    s.pop()
    t.pop()
    s = list(map(int, s))
    t = list(map(int, t))

    p = 0
    for i in range(1, 10):
        for j in range(1, 10):
            s_c = s.copy()
            t_c = t.copy()
            s_c.append(i)
            t_c.append(j)
            if is_possible(k, s_c, t_c) is False:
                continue

            takahashi_point = calc_point(k, s_c)
            aoki_point = calc_point(k, t_c)
            if takahashi_point > aoki_point:
                remain_i = k - s.count(i) - t.count(i)
                remain_j = k - s.count(j) - t.count(j)

                if i == j:
                    p += remain_i * (remain_i - 1) / ((9*k-8) * (9*k-9))
                else:
                    p += remain_i * remain_j / ((9*k-8) * (9*k-9))

    print(p)


if __name__ == '__main__':
    main()
