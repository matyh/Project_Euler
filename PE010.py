# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
import math
import time
import timeit


# Sieve of Eratosthenes, inefficient, runtime 0.11529638199999999
def sieveOfEratosthenes(n):
    numbers = [i for i in range(2, n + 1)]
    for number in numbers:
        if type(number) is int:
            for i in range(2 * number, n + 1, number):
                numbers[i-2] = 'x'
    listOfPrimes = list(filter(lambda x: x != 'x', numbers))
    # either
    sum = 0
    for i in listOfPrimes:
        sum += i
    return sum
    # return sum(listOfPrimes)


# better sieve of Eratosthenes, runtime 0.021684703999999985
def sieveOfErathosthenes2(n):
    last = int(math.sqrt(n))
    # make list of boolean for each number
    sieve = [True] * (n - 1)
    # mark out even numbers except for 2
    for i in range(2, n, 2):
        sieve[i] = False
    # iterate through all odd numbers (as all even were eliminated)
    for i in range(1, last-1, 2):
        if sieve[i]:
            # go through numbers from i^2 because any previous multiple of i
            # has a prime divisor less than i and has already been crossed out
            for j in range((i+2)**2-2, n-1, 2*(i+2)):
                sieve[j] = False
    sum = 0
    for i in range(0, n-1):
        if sieve[i]:
            sum += i+2
    return sum


# sieve with list, runtime 0.06810612800000002
def sieveOfErathosthenes3(n):
    last = int(math.sqrt(n))
    # make list of boolean for each number
    sieve = [[x, True] for x in range(2, n+1)]
    # mark out even numbers except for 2
    # starts with 4-2 because no 4 has index 2
    for i in range(2, n-1, 2):
        sieve[i][1] = False
    # iterate through all odd numbers (as all even were eliminated)
    for i in range(1, last+1, 2):
        if sieve[i][1]:
            # go through numbers from i^2 because any previous multiple of i
            # has a prime divisor less than i and has already been crossed out
            for j in range(sieve[i][0]**2-2, n-1, 2*sieve[i][0]):
                sieve[j][1] = False
    sum = 0
    # print(sieve)
    for i in sieve:
        if i[1]:
            sum += i[0]
    return sum


# sieve with dict, runtime 0.06761549800000001
def sieveOfErathosthenes4(n):
    last = int(math.sqrt(n))
    # generate dict of numbers with boolean flag default to true
    sieve = {}
    for x in range(2, n+1):
        sieve[x] = True
    # mark out even numbers except for 2
    for i in range(4, n+1, 2):
        sieve[i] = False
    # iterate through all odd numbers (as all even were eliminated)
    for i in range(3, last+1, 2):
        if sieve[i]:
            # go through numbers from i^2 because any previous multiple of i
            # has a prime divisor less than i and has already been crossed out
            for j in range(i**2, n+1, 2*i):
                sieve[j] = False
    suma = 0
    for i in range(2, n+1):
        if sieve[i]:
            suma += i
    return suma


limit = 200000

# start = time.time()
# a = sieveOfEratosthenes(limit)
# print("my first, inefficient", a)
# end = time.time()
# print(end - start)
# #
# start = time.time()
# a = sieveOfErathosthenes2(limit)
# print("second, list but without values", a)
# end = time.time()
# print(end - start)

# start = time.time()
# c = sieveOfErathosthenes3(limit)
# print("3 / with list", c)
# end = time.time()
# print(end - start)
#
# start = time.time()
# c = sieveOfErathosthenes4(limit)
# print("4 - with dict", c)
# end = time.time()
# print(end - start)

# start = time.time()
# a = [x for x in range(limit)]
# print(time.time() - start)

# start = time.time()
# a = {}
# for x in range(limit):
#     a[x] = True
# print(time.time() - start)


# testing runtime
# print('first', timeit.timeit('sieveOfEratosthenes(limit)', 'from __main__ import sieveOfEratosthenes, limit', number=50) / 50)
# print('second', timeit.timeit('sieveOfErathosthenes2(limit)', 'from __main__ import sieveOfErathosthenes2, limit', number=50) / 50)
print('list', timeit.timeit('sieveOfErathosthenes3(limit)', 'from __main__ import sieveOfErathosthenes3, limit', number=50) / 50)
print('dics', timeit.timeit('sieveOfErathosthenes4(limit)', 'from __main__ import sieveOfErathosthenes4, limit', number=50) / 50)

