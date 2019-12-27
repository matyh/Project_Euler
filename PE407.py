"""
If we calculate a^2 mod 6 for 0 ≤ a ≤ 5 we get: 0,1,4,3,4,1.

The largest value of a such that a^2 ≡ a mod 6 is 4.
Let's call M(n) the largest value of a < n such that a^2 ≡ a (mod n).
So M(6) = 4.

Find ∑ M(n) for 1 ≤ n ≤ 10^7.
"""


def m(n):
    if n == 1:
        return 0
    for a in range(n - 1, 0, -1):
        if a ** 2 % n == a:
            return a


def m_sum(lower, upper):
    """
    :param lower: lower limit of n
    :param upper: upper limit of n
    :return:
    """
    result = 0
    for n in range(lower, upper+1):
        result += m(n)
        print(n)  # to see where in the range we are currently
    return result


print(m_sum(1, 10000000))

# for n in range(1, 37):
#     res = m(n)
#     print(f"{n}: {res}")
