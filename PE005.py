import math


def smallestMultiple(lbound, ubound):
    number = ubound
    isMultiple = False
    while not isMultiple:
        for divisor in range(lbound, ubound + 1):
            if number % divisor != 0:
                number += ubound
                break
        else:
            isMultiple = True
    return number


# print(math.factorial(20))
print(smallestMultiple(1, 20))
