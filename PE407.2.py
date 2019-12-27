"""
If we calculate a^2 mod 6 for 0 ≤ a ≤ 5 we get: 0,1,4,3,4,1.

The largest value of a such that a^2 ≡ a mod 6 is 4.
Let's call M(n) the largest value of a < n such that a^2 ≡ a (mod n).
So M(6) = 4.

Find ∑ M(n) for 1 ≤ n ≤ 10^7.
"""


def m(n):
    lis = []
    if n == 1:
        return 0
    for a in range(n - 1, 0, -1):
        if a ** 2 % n == a:
            lis.append(a)
            # return a
    return sorted(lis)


def m_sum(lower, upper):
    """
    :param lower: lower limit of n
    :param upper: upper limit of n
    :return:
    """
    result = 0
    for n in range(upper, lower - 1, -1):
        add = m(n)
        result += add
    return result


# print(m_sum(1, 36))

# for n in range(1, 37):
#     res = m(n)
#     print(f"{n}: {res}")

for a in range(1, 21):
    lis = [x for x in range(1, a)]
    sqr = [x**2 for x in range(1, a)]
    mod = [x**2 % a for x in range(1, a)]
    print(a)
    print(lis)
    print(sqr)
    print(mod)
    print(m(a), end='\n\n')
