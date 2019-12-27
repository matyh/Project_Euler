import math


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


def divisors(n):
    divList = []
    sqrt = int(math.sqrt(n))
    if n % 2 == 0:
        divList.append(2)
    for i in range(2, sqrt + 1):
        if n % i == 0:
            temp = int(n / i)
            divList += [i, temp]
    return sorted(divList)


def divisors2(n):
    # dle overview, ale vybírá to jen některá čísla ze všech dělitelů -
    # primes i non-primes
    divList = []
    number = n
    factor = 2
    while number > 1:
        if number % factor == 0:
            number /= factor
            if factor not in divList:
                divList.append(factor)
            divList.append(number)
        else:
            factor += 1
    return divList


def divisor(number):
    # dle overview, moc tomu nerozumímm
    if number % 2 == 0:
        lastFactor = 2
        number /= 2
        while number % 2 == 0:
            number /= 2
    else:
        lastFactor = 1
    factor = 3
    maxFactor = int(math.sqrt(number)) + 1
    while number > 1 and factor <= maxFactor:
        if number % factor == 0:
            number /= factor
            maxFactor = int(math.sqrt(number)) + 1
        factor += 2
    if number == 1:
        return lastFactor
    else:
        return number


number = 600851475143
print("divisor", divisor(number))
print("divisors", divisors(number))
print("divisors2", divisors2(number))
for i in divisors2(number):
    if isPrime(i):
        print(i, "is Prime")
    else:
        print(i, "is not Prime")
highest = 1
for number in divisors(number):
    if isPrime(number) and number > highest:
        highest = number
print(highest)
