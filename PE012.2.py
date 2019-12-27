import math
from datetime import time


def divisors(n):
    # get factors and their counts

    # in the first part we find factor primes dividing n, saving them in the
    # dict with count of how many times the reminder is divisible by the
    # prime, so when we have number 156, the dict will be {2:2, 3:1, 13:1}
    # as 2 * 2 * 3 * 13 = 156

    factors = {}
    # copy of n so we will not mutate the original argument
    nn = n
    i = 2
    # same as while i <= sqrt(n)
    while i*i <= nn:
        while nn % i == 0:
            # if nn is divisible by i include i in the dict and count how many
            # times it is dividable
            factors[i] = factors.get(i, 0) + 1
            nn //= i
        # ifi the reminder is not divisible by the i anymore, increase i
        i += 1
    if nn > 1:
        factors[nn] = factors.get(nn, 0) + 1

    primes = list(factors.keys())

    # generates factors from primes[k:] subset
    def generate(k):
        if k == len(primes):
            yield 1
        else:
            rest = generate(k+1)
            prime = primes[k]
            for factor in rest:
                prime_to_i = 1
                # prime_to_i iterates prime**i values, i being all possible exponents, iteruje o jedno vice ney je v dict
                for _ in range(factors[prime] + 1):
                    yield factor * prime_to_i
                    prime_to_i *= prime

# in python3, `yield from generate(0)` would also work
    for factor in generate(0):
        yield factor


div = []
for i in divisors(156):
   div.append(i)
print(div)
