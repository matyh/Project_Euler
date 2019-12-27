import math, time


def isPrime(n):
    """
    :param n: int, number to check if prime
    :return: boolean whether prime or not
    """
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    sqrt = int(math.sqrt(n))
    for i in range(3, sqrt + 1, 2):
        if n % i == 0:
            return False
    return True


def genPrimes():
    number = 0
    while True:
        if isPrime(number):
            yield number
        number += 1


# count = 0
# for prime in genPrimes():
#     count += 1
#     if count == 10001:
#         print(prime)

# print(isPrime(999))