# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

below = 10000000
result = 0

for number in range(1, below):
    if number % 3 == 0 or number % 5 == 0:
        result += number

print(result)

# To get a more efficient solution you could also calculate the sum of the
# numbers less than1000 that are divisible by 3, plus the sum of the numbers
# less than1000 that are divisible by 5. But as you have summed numbers
# divisible by 15 twice you would have to subtract the
# sum of the numbers divisible by 15.
#
# Let’s look at the details of our function and take as example n=3.
# We would have to add:
# 3+6+9+12+......+999=3*(1+2+3+4+...+333)
# For n=5 we would get:
# 5+10+15+...+995=5*(1+2+....+199)
# Now note that 199=995/5 but also 999/5 rounded down to the nearest integer.
# Also note that 1+2+3+...+p=1/2*p*(p+1)

last = below - 1


def sumDivBy(divisor):
    p = last // divisor
    return divisor * (1 / 2 * p * (p + 1))


print(sumDivBy(3) + sumDivBy(5) - sumDivBy(15))
