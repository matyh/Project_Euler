# A Pythagorean triplet is a set of three natural numbers, a < b < c,
# for which, a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math


def findTriplet():
    a, b, c = 1, 2, 335
    for x in range(1, 333):
        a = x
        for y in range(x+1, 500):
            b = y
            for z in range(335, 998):
                c = z
                if a < b < c and a + b + c == 1000 and a**2 + b**2 == c**2:
                    return a, b, c


# a = <1, 332>
# b = <2, 499>
# c = <335, 997>

result = findTriplet()
# result = (200, 375, 425)
print(result)
foo = 1
for i in result:
    foo *= i
print(foo)
