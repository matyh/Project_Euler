# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


def isPalindrome(n):
    """
    :param n: int, number to check if palindrome
    :return: True if palindrome, else False
    """
    reverse = ''
    for digit in str(n)[::-1]:
        reverse += digit
    return n == int(reverse)


numbers = []
for i in range(999, 99, -1):
    numbers.append(i)
# print(numbers)

# print(isPalindrome(9009))
# print(isPalindrome(9595))
# print(isPalindrome(1010101))

largest = 0
for i in numbers:
    for j in numbers:
        guess = i * j
        if isPalindrome(guess) and guess > largest:
            largest = guess

print(largest)

