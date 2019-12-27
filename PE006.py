
n = 100

sumOfSqr = 0
sqrOfSum = 0
for i in range(1, n + 1):
    sumOfSqr += i ** 2
    sqrOfSum += i
print(sqrOfSum ** 2 - sumOfSqr)

# much faster, but differs with higher n, not sure why
sumOfSqr = n * (n + 1) / 2
sqrOfSum = (2 * n + 1) * (n + 1) * n / 6
print(sumOfSqr ** 2 - sqrOfSum)
