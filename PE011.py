"""
In the 20×20 grid in the PE011.txt file, four numbers along a diagonal line have been marked in red.

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
"""


def process_file():
    """
    Process the PE011.txt file into array
    :return: list of rows as lists of ints from the file
    """
    file = open('PE011.txt', 'r')
    array = []
    for line in file:
        row = list(map(int, line.split()))
        array.append(row)
    return array


def find_product(array):
    """
    Finds product of four adjacent numbers in the same direction (up down,
    left, right, diagonal) in the array
    :param list array: array of numbers 20x20
    :return: maximal product of four adjacent numbers in the array
    """
    maxProduct = 0
    # horizontal
    for y in range(20):
        for x in range(20-4):
            product = array[y][x] * \
                      array[y][x + 1] * \
                      array[y][x + 2] * \
                      array[y][x + 3]
            if product > maxProduct:
                maxProduct = product
    # vertical
    for y in range(20-4):
        for x in range(20):
            product = array[y][x] * \
                      array[y + 1][x] * \
                      array[y + 2][x] * \
                      array[y + 3][x]
            if product > maxProduct:
                maxProduct = product
    # diagonal uppper-left to lower-right
    for y in range(20 - 4):
        for x in range(20 - 4):
            product = array[y][x] * \
                      array[y + 1][x + 1] * \
                      array[y + 2][x + 2] * \
                      array[y + 3][x + 3]
            if product > maxProduct:
                maxProduct = product
    # diagonal upper-right to lower-left
    for y in range(20-4):
        for x in range(3, 20):
            product = array[y][x] * \
                      array[y + 1][x - 1] * \
                      array[y + 2][x - 2] * \
                      array[y + 3][x - 3]
            if product > maxProduct:
                maxProduct = product
    return maxProduct


print(find_product(process_file()))
