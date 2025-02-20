# Each new term in the Fibonacci sequence is generated by adding the previous
# two terms. By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.

result = 0
fibList = [1, 2]
while fibList[-1] + fibList[-2] < 4000000:
    fibList.append(fibList[-1] + fibList[-2])
for number in fibList:
    if number % 2 == 0:
        result += number

print(fibList)
print(result)